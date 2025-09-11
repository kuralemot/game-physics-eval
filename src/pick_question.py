import os
import json
import random
import glob
import shutil
from pathlib import Path
from bs4 import BeautifulSoup as Soup

#For pilot Study

def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def LoadXMl(file_name):
    with open(file_name, 'r') as f:
        data = f.read()
    Bs_data = Soup(data, "xml")
    return Bs_data

def FindBlock(file_name, file_type="xml"):
    
    if file_type == "xml":
        Bs_data = LoadXMl(file_name)
    
    Blocks = Bs_data.find_all("Block")
    
    return Blocks

def load_config(task_num, subtask=None):
    summary_data = None
    summary_mapping = None
    print(f"Loading configuration for task {task_num} with subtask {subtask}")
    if task_num == 1:
        #load json file for task 1
        summary_data = load_json('./data/task_1/summary.json')
        
        summary_mapping = {item['id']: {
            'correct_answer': item['is_stable']
        } for item in summary_data['gt']}
        return summary_mapping
    elif task_num == 2:
        #load json file for task 2s
        summary_data = load_json('./data/task_2/summary.json')
        
        # Create a mapping from ID to metadata
        summary_mapping = {item['id']: {
            'task_mode': item['task_mode'],
            'correct_answer': item['correct_answer'],
            'options_count': len(item['options']),
            'options': item['options']
        } for item in summary_data['gt']}
        
        return summary_mapping
        
    elif task_num == 3:
        #load json file for task 3
        summary_data = load_json('./data/task_3/summary.json')
        
         # Create a mapping from ID to metadata
        summary_mapping = {item['id']: {
            'task_mode': item['task_mode'],
            'correct_answer': item['correct_answer'],
            'options_count': len(item['options']),
            'options': item['options']
        } for item in summary_data['gt']}
        
        return summary_mapping
    else:
        raise ValueError(f"Unsupported task number: {task_num}")

def case2(mapping, subtask=None):
    all_qid = []
    for item_id, metadata in mapping.items():
        if metadata['options_count'] == 4: 
            answer = metadata['correct_answer']
            for option in metadata['options']:
                if answer == option['id']:
                    if option['block_count'] == 12:
                        all_qid.append(item_id)
    return all_qid

def case1(mapping, subtask=None):
    all_qid = []
    
    all_qid = []
    qid_stable = []
    qid_unstable = []
    folder_path = './data/task_1/xml/*.xml'
    xml_files = glob.glob(folder_path)
    for file_path in xml_files:
        file = LoadXMl(file_path)
        blocks = FindBlock(file_path, file_type="xml")
        
        if len(blocks) == 12:
            _file_name = os.path.basename(file_path)
            file_name = _file_name.split('.')[0]
            file_id, task = file_name.split('_')
            
            if task == "stable":
                qid_stable.append(file_id)
            elif task == "unstable":
                qid_unstable.append(file_id)
            
    rand_five_stable = random.sample(qid_stable, 5)
    rand_five_unstable = random.sample(qid_unstable, 5)
    
    all_qid = rand_five_stable + rand_five_unstable
    
    return all_qid

def case3(mapping, subtask=None):
    
    all_qid = []
    all_qid_block = []
    all_qid_id = []
    all_qid_level = []
    
    for item_id, metadata in mapping.items():
        answer = metadata['correct_answer']
        for option in metadata['options']:
            if answer == option['id']:
                if option['block_count'] == 12:
                    if 'block' in metadata['task_mode']:
                        all_qid_block.append(item_id)
                    elif 'id' in metadata['task_mode']:
                        all_qid_id.append(item_id)
                    elif 'level' in metadata['task_mode']:
                        all_qid_level.append(item_id)
    
    random_five_bl = random.sample(all_qid_block, 5)
    random_five_id = random.sample(all_qid_id, 5)
    random_five_lvl = random.sample(all_qid_level, 5)

    all_qid = random_five_bl + random_five_id + random_five_lvl
    
    
    return all_qid

def pick(task_num, summary_mapping, subtask=None):

    if task_num == 1:
        all_qid = case1(summary_mapping)
    elif task_num == 2:
        all_qid = case2(summary_mapping)
    elif task_num == 3:
        all_qid = case3(summary_mapping)

    return all_qid
     
    
def getImageQn(task_num, qids):
    
    src_folder = Path('./data')
    dst_folder = Path('./questions')
    
    if task_num == 1:
        src_folder = src_folder / 'task_1' / 'image'
        dst_folder = dst_folder / 'task_1'  
        
    elif task_num == 2:
        src_folder = src_folder / 'task_2' / 'image'
        dst_folder = dst_folder / 'task_2'
        
    elif task_num == 3:
        src_folder = src_folder / 'task_3' / 'image'
        dst_folder = dst_folder / 'task_3'
        
    else:
        raise ValueError(f"Unsupported task number: {task_num}")
    
    for image_path in src_folder.glob('*.png'):
        _id = image_path.stem.split('_')[0]
        if _id in qids:
            shutil.copy(image_path, dst_folder)

def main():
    
    json_file = Path('./questions/question.json')
    
    if json_file.exists():
        print(f"JSON file {json_file} exists.")
        return
    
    else:
        
        base_path = Path('./questions')
        if not base_path.exists():
            base_path.mkdir()

        results = {}
        
        for task_num in range(1, 4):
            
            summary_mapping = load_config(task_num)
            qa = pick(task_num, summary_mapping)
            
            print(f"Task {task_num} selected questions: {qa}")
            
            task_path = Path(str(base_path) + "/task_" + str(task_num))
            if not task_path.exists():
                task_path.mkdir()
            getImageQn(task_num, qa)
            results[f"task_{task_num}"] = qa
            
        # Save to JSON file
        with open( json_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=4)

if __name__=="__main__":   
    main()