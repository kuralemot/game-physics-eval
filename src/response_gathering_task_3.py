import argparse
from utils import file_manager as fm
from pathlib import Path
from lm import *
from pydantic import BaseModel
from typing import List, Dict, Any
import os

prompt_dir=Path('./prompts')

class Answer(BaseModel):
  reason: str
  answer: str

def get_llm(model_name:str) -> LMBase:
    if 'studio' in model_name:
        return OllamaLM(model_name=model_name)
    elif 'claude' in model_name:
        return AnthropicLM(model_name=model_name)
    elif 'gpt' in model_name:
        return OpenAILM(model_name=model_name)
    else:
        return OllamaLM(model_name=model_name)


def format_group_input(temporal_groups: Dict[str, List[Dict]], data_type: str) -> str:
    
    formatted_parts = []
    for file_path in temporal_groups['initial']:
        content = fm.read_text(file_path['path'])
        formatted_parts.append(
            f"Initial State  \n'''{data_type}\n{content}\n'''\n"
        )
    formatted_parts.append(fm.format_file_input(temporal_groups['options']))
   
    return "\n".join(formatted_parts)

def get_file_group(s_dir: Path, item_id: str, item: List[Dict]) -> List[Dict]:
    file_group = {
        'initial': [],  # t=0 files
        'options': []   # t=10 files
    }
    type_map = {
        'xml': 'xml',
        'json': 'json',
        'image': 'png'
    }
    
    fn_1 = f"{item_id}_t=0"
    fn_2 = f"{item_id}_t=10"
    
    all_files = os.listdir(s_dir)
    
    #1_t=0_D_stable n 1_t=10_A_unstable
    
    for filename in all_files:
        if s_dir.stem  in type_map:
            ext = type_map[s_dir.stem]
            
            for option in item['options']:
                stability = 'stable' if option['is_stable'] else 'unstable'
                option_id = option['id']
                
                fnn_2 = f"{fn_2}_{option_id}_{stability}.{ext}"
                if fnn_2 == filename:
                    file_path = s_dir / fnn_2  
                    if file_path.exists():
                        file_group['options'].append({
                            'filename': filename,
                            'option_id': option['id'], 
                            'stability': stability,
                            'path': file_path, 
                            'ext': ext
                        })
                
                if item['correct_answer'] == option['id']:
                    fnn_1 = f"{fn_1}_{item['correct_answer']}_{stability}.{ext}"
                    if fnn_1 == filename:
                        file_path = s_dir / filename
                        if file_path.exists():
                            file_group['initial'].append({
                                'filename': filename,
                                'correct': item['correct_answer'],
                                'stability': stability,
                                'path': file_path
                            })
    return file_group
    
def gather_responses(llm:LMBase, source_dir:str, dest_dir:str, data_type:str, pe_type:str, temperature:float):
    s_dir=Path(source_dir, data_type)
    d_dir=Path(dest_dir, data_type)
    d_dir.parent.mkdir(parents=True, exist_ok=True)
    s_files=[f for f in s_dir.iterdir() if f.is_file()]
    llm.set_output_format(Answer)

    # Load summary file
    summary = fm.load_summary_file(source_dir)        
    
    # Prompt template
    pt_path = prompt_dir / pe_type / f"{data_type}.txt"
    prompt_template = fm.read_text(pt_path)
     
    for i, item in enumerate(summary['gt']):
        group_id  = item['id']
                
        print(f'gathering>>{llm.model_name()}-{data_type}-{pe_type}:{group_id}')
        
        # Get all files
        file_group = get_file_group(s_dir, group_id, item)
        
        if "image" in data_type:
            image_paths = [str(f['path']) for f in file_group['initial'] + file_group['options']]
            prompt=llm.build_prompt([prompt_template], image_paths)
            response=llm.run_prompt(temperature=temperature, messages=prompt)
            
        else:
            formatted_input = format_group_input(file_group, data_type)
            prompt=llm.build_prompt([prompt_template.replace('<input>', formatted_input)])
            response=llm.run_prompt(temperature=temperature, messages=prompt)
            
        d_filepath=d_dir.joinpath(f"{group_id}_{item['correct_answer']}.json")
        fm.write_json(path=d_filepath, data=response, compressed=False)   
    pass

if __name__=="__main__":    
    arg_parser = argparse.ArgumentParser(prog="response-gathering", description="response-gathering")
    arg_parser.add_argument("-source", type=str, required=True)
    arg_parser.add_argument("-destination", type=str, required=True)
    arg_parser.add_argument("-data_type", type=str, required=True, help="data type: [\"function\", \"grid\", \"image\", \"level\", \"xml\"]")
    arg_parser.add_argument("-pe_type", type=str, required=True, help="data type: [\"zero_shot\"]")
    arg_parser.add_argument("-llm", type=str, required=False, default='llava:7b')
    arg_parser.add_argument("-temperature", type=float, required=False, default=0.0)
    args = arg_parser.parse_args()

    mylm=get_llm(args.llm)
    gather_responses(llm=mylm, source_dir=args.source, dest_dir=args.destination, data_type=args.data_type, pe_type=args.pe_type, temperature=args.temperature)