import argparse
from utils import file_manager as fm
from pathlib import Path
from lm import *
from pydantic import BaseModel

prompt_dir=Path('./prompts')

class Answer(BaseModel):
  reason: str
  answer: str

def get_llm(model_name:str) -> LMBase:
    if 'ollama' in model_name:
        return OllamaLM(model_name=model_name)
    elif 'claude' in model_name:
        return AnthropicLM(model_name=model_name)
    elif 'gpt' in model_name:
        return OpenAILM(model_name=model_name)
    else:
        return LMStudio(model_name=model_name)

def gather_responses(llm:LMBase, source_dir:str, dest_dir:str, data_type:str, pe_type:str, temperature:float):
    s_dir=Path(source_dir, data_type)
    d_dir=Path(dest_dir, data_type)
    d_dir.parent.mkdir(parents=True, exist_ok=True)
    s_files=[f for f in s_dir.iterdir() if f.is_file()]
    llm.set_output_format(Answer)

    pt_path=Path(prompt_dir, pe_type, f'{data_type}.txt')
    prompt_template=fm.read_text(pt_path)
    for i, s_filepath in enumerate(s_files):
        print(f'gathering>>{llm.model_name()}-{data_type}-{pe_type}:{i+1}')
        if "image" in data_type:
            prompt=llm.build_prompt([prompt_template], [str(s_filepath)])
            response=llm.run_prompt(temperature=temperature, messages=prompt)
        else:
            input_data=fm.read_text(s_filepath)
            # prompt=prompt_template.replace('<input>', input_data)
            # response=llm.run_prompt(temperature=temperature, 
            #                         messages=[{'role':'user', 'content':prompt}])
            
            prompt=llm.build_prompt([prompt_template.replace('<input>', input_data)])
            response=llm.run_prompt(temperature=temperature, messages=prompt)
        d_filepath=d_dir.joinpath(f'{s_filepath.stem}.json')
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