# run_all.py
import os

commands = [
    ('xml', 'task_1/zero-shot'),
    ('json', 'task_1/zero-shot'),
    ('image', 'task_1/zero-shot-cot'),
    ('xml', 'task_1/zero-shot-cot'),
    ('json', 'task_1/zero-shot-cot'),
    ('image', 'task_1/zero-shot-cot'),
    ('xml', 'task_1/null-shot'),
    ('json', 'task_1/null-shot'),
    ('image', 'task_1/null-shot'),
    ('xml', 'task_1/null-shot-cot'),
    ('json', 'task_1/null-shot-cot'),
    ('image', 'task_1/null-shot-cot')
]

for data_type, pe_type in commands:
    dest = f"./responses/task_1/{pe_type.split('/')[-1]}/gpt_4o"
    cmd = (
        f"python ./src/response_gathering.py -source ./data/task_1/ "
        f"-destination {dest} -data_type {data_type} -pe_type {pe_type} "
        f"-llm gpt-4o-2024-11-20 -temperature 0"
    )
    print(f"Running: {cmd}")
    os.system(cmd)
