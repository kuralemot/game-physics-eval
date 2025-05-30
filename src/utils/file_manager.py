import json
import shutil
import pandas as pd
import utils.logger as logger
import glob
import os
from lm.lm_response import LMResponse
from lm.lm_embeddings import LMEmbeddings
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any

def get_files_with_extension(directory, extension):
    files = glob.glob(os.path.join(directory, f"*.{extension}"))
    return files

def crawl_files(directory:str, extensions:list[str]):
    return [str(file) for file in Path(directory).rglob('*') if file.suffix.lower() in extensions]

def get_file_name_without_extension(file_path):
    file_name, _ = os.path.splitext(os.path.basename(file_path))
    return file_name

def get_file_extension(file_path):
    _, extension = os.path.splitext(file_path)
    return extension

def write_text(path, content):
    try:
        dir_name=os.path.dirname(path)
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
            
        with open(path, "w", encoding = "utf-8") as f:
            f.write(content)
            f.close()
    except Exception as e:
        print(str(e))        
        logger.error(f"write_text error: {e}")

def read_text(path):
    try:
        with open(path, "r", encoding = "utf-8") as f:
            result = f.read()
            f.close()
            return result
    except Exception as e:
        print(str(e))        
        logger.error(f"read_text error: {e}")
        return ""

def write_json(path, data, compressed=False):
    try:
        dir_name=os.path.dirname(path)
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

        if compressed:
            json_object = json.dumps(data, cls=MyJSONEncoder)
        else:
            json_object = json.dumps(data, indent = 4, cls=MyJSONEncoder, default=lambda o: o.__dict__)
            
        # Writing to sample.json
        with open(path, "w",encoding = "utf-8") as f:
            f.write(json_object)
            f.close()
    except Exception as e:
        print(str(e))        
        logger.error(f"write_json error: {e}")

def read_json(path):
    try:
        with open(path, encoding = "utf-8") as f:
            data = json.load(f)
            f.close()
            return data
    except Exception as e:
        print(str(e))        
        logger.error(f"read_json error: {e}")
        return []
    
def write_csv(path, data, header):
    try:
        dir_name=os.path.dirname(path)
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

        df = pd.DataFrame(data, columns = header)
        df.to_csv(path, index = False)
    except Exception as e:
        print(str(e))        
        logger.error(f"write_csv error: {e}")

def read_csv(path):
    try:
        df = pd.read_csv(path, encoding="utf-8")
        data = df.values.tolist()
        return data
    except Exception as e:
        print(str(e))        
        logger.error(f"read_csv error: {e}")
        return []
    
def copy_file(src_file, dst_file):
    try:
        target_dir=os.path.dirname(dst_file)
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        shutil.copyfile(src_file, dst_file)
    except Exception as e:
        print(str(e))        
        logger.error(f"copy_file error: {e}")

def get_timestamp():
    return datetime.now().strftime("%Y%m%d%H%M")


#for task 2
def get_prompt_path(prompt_dir: Path, task_name: str, pe_type: str, data_type: str, task_mode: str) -> Path:
    # Determine stability suffix based on task_mode
    stability_suffix = 'unstable' if 'unstable' in task_mode else 'stable'
    prompt_filename = f"{data_type}_{stability_suffix}.txt"
    print(f"Prompt filename: {prompt_filename}")
    return prompt_dir / pe_type / prompt_filename


def load_summary_file(source_dir: str) -> Dict[str, Any]:
    summary_path = Path(source_dir, 'summary.json')
    
    return read_json(summary_path)

def get_file_group(s_dir: Path, item_id: str, options: List[Dict]) -> List[Dict]:
    file_group = []
    for option in options:
        print(f"option: {option}")
        option_id = option['id']
        stability = 'stable' if option['is_stable'] else 'unstable'
        # Check for both xml and json files
        for ext in ['xml', 'json', 'png']:
            filename = f"{item_id}_{option_id}_{stability}.{ext}"
            file_path = s_dir / filename
            if file_path.exists():
                file_group.append({
                    'option_id': option_id,
                    'stability': stability,
                    'path': file_path,
                    'ext': ext
                })
    return file_group

def format_file_input(file_group: List[Dict]) -> str:
    formatted_parts = []
    for file_info in file_group:
        content = read_text(file_info['path'])
        formatted_parts.append(
            f"{file_info['option_id']}.\n'''{file_info['ext']}\n{content}\n'''\n"
        )
    return "\n".join(formatted_parts)


#not used
def get_few_shot_images(s_filepath: Path, s_dir: Path) -> list[str]:
    
    all_images = list(s_dir.glob('*.*'))
    
    # Exclude the current image
    other_images = [img for img in all_images if img != s_filepath]
    
    stable_img = None
    unstable_img = None
    
    for img in other_images:
        if "_stable" in img.stem and stable_img is None:
            stable_img = img
        elif "_unstable" in img.stem and unstable_img is None:
            unstable_img = img
        if stable_img and unstable_img:
            break
    
    # list with new order: stable, unstable, original
    if stable_img and unstable_img:
        return [str(stable_img), str(unstable_img), str(s_filepath)]
    return [str(s_filepath)]

class MyJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, LMResponse):
            return obj.dict()
        elif isinstance(obj, LMEmbeddings):
            return obj.dict()
        return super().default(obj)