import os

tasks = ['task_1', 'task_2', 'task_3']
pe_types = ['zero-shot', 'zero-shot-cot', 'null-shot', 'null-shot-cot']
models_folder = ['gpt_4o', 'gpt_4-1-mini', 'qwen2.5-vl-3b', 'qwen2.5-vl-7b', 'gemma3-4b', 'llava-7b']

for task in tasks:
    for pe_type in pe_types:
        for model in models_folder:
            source = fr".\responses\{task}\{pe_type}\{model}"
            dest = fr".\evaluation\{task}\{pe_type}\{model}"
            cmd = (
                f"python ./src/evaluation.py "
                f"-source {source} "
                f"-destination {dest}"
            )
            print(f"Running: {cmd}")
            
            # Run the command and check for errors
            return_code = os.system(cmd)
            if return_code != 0:
                print(f"❌ Error running command (exit code: {return_code}): {cmd}")
                continue  # Skip to the next iteration if there's an error