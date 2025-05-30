import random
import shutil
import re
from utils import file_manager as fm
from pathlib import Path

def main():
    target_dir=Path('./data')
    dir_path=Path('./raw_data')
    directories=[d for d in dir_path.iterdir() if d.is_dir()]
    for dir in directories:
        dir_id=dir.name
        function_files=[f for f in fm.crawl_files(dir, '.txt') if 'function' in f]
        stable_functions=[[Path(f), Path(f).read_text()] for f in function_files if 'function-stable-' in f]
        unstable_functions=[[Path(f), Path(f).read_text()] for f in function_files if 'function-unstable-' in f]
        
        seen=set()
        stable_functions=[content for content in stable_functions if not (content[1] in seen or seen.add(content[1]))]

        seen=set()
        unstable_functions=[content for content in unstable_functions if not (content[1] in seen or seen.add(content[1]))]

        stable_functions=random.sample(stable_functions, 10)
        unstable_functions=random.sample(unstable_functions, 10)
        functions=[]
        functions.append(['stable', [f[0] for f in stable_functions]])
        functions.append(['unstable', [f[0] for f in unstable_functions]])
        
        for fpair in functions:
            label=fpair[0]
            for i, f in enumerate(fpair[1]):
                t_filename=str(f.stem)
                grid_filename=f"{t_filename.replace('function-', 'grid-')}.txt"
                img_filename=f"{t_filename.replace('function-', 'image-')}_raw.png"
                lv_filename=f"{t_filename.replace('function-', 'level-')}.xml"
                xml_filename=f"{t_filename.replace('function-', 'xml-')}.xml"

                s_func=f
                s_grid=Path(dir, grid_filename)
                s_img=Path(dir, img_filename)
                s_lv=Path(dir, lv_filename)
                s_xml=Path(dir, xml_filename)

                d_func=target_dir.joinpath('function', f'{label}-{dir_id}-{i+1}.txt')
                d_grid=target_dir.joinpath('grid', f'{label}-{dir_id}-{i+1}.txt')
                d_img=target_dir.joinpath('image', f'{label}-{dir_id}-{i+1}.png')
                d_lv=target_dir.joinpath('level', f'{label}-{dir_id}-{i+1}.xml')
                d_xml=target_dir.joinpath('xml', f'{label}-{dir_id}-{i+1}.xml')

                d_func.parent.mkdir(parents=True, exist_ok=True)
                d_grid.parent.mkdir(parents=True, exist_ok=True)
                d_img.parent.mkdir(parents=True, exist_ok=True)
                d_lv.parent.mkdir(parents=True, exist_ok=True)
                d_xml.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy(s_func, d_func)
                shutil.copy(s_grid, d_grid)
                shutil.copy(s_img, d_img)
                shutil.copy(s_lv, d_lv)
                shutil.copy(s_xml, d_xml)
        print(f'{dir.name} >> stable:{len(stable_functions)} || unstable:{len(unstable_functions)}')
        pass
    pass

if __name__=="__main__":
    main()