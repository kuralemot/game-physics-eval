#!/bin/bash

python ./src/response_gathering.py -source "./data/task_1/" -destination "./responses/task_1/zero-shot/gpt_4o" -data_type "xml" -pe_type "task_1/zero-shot" -llm "gpt-4o-2024-08-06" -temperature 0
python ./src/response_gathering.py -source "./data/task_1/" -destination "./responses/task_1/zero-shot/gpt_4o" -data_type "json" -pe_type "task_1/zero-shot" -llm "gpt-4o-2024-08-06" -temperature 0
python ./src/response_gathering.py -source "./data/task_1/" -destination "./responses/task_1/zero-shot/gpt_4o" -data_type "image" -pe_type "task_1/zero-shot" -llm "gpt-4o-2024-08-06" -temperature 0

python ./src/response_gathering.py -source "./data/task_1/" -destination "./responses/task_1/zero-shot-cot/gpt_4o" -data_type "xml" -pe_type "task_1/zero-shot-cot" -llm "gpt-4o-2024-08-06" -temperature 0
python ./src/response_gathering.py -source "./data/task_1/" -destination "./responses/task_1/zero-shot-cot/gpt_4o" -data_type "json" -pe_type "task_1/zero-shot-cot" -llm "gpt-4o-2024-08-06" -temperature 0
python ./src/response_gathering.py -source "./data/task_1/" -destination "./responses/task_1/zero-shot-cot/gpt_4o" -data_type "image" -pe_type "task_1/zero-shot-cot" -llm "gpt-4o-2024-08-06" -temperature 0

python ./src/response_gathering.py -source "./data/task_1/" -destination "./responses/task_1/null-shot/gpt_4o" -data_type "xml" -pe_type "task_1/null-shot" -llm "gpt-4o-2024-08-06" -temperature 0
python ./src/response_gathering.py -source "./data/task_1/" -destination "./responses/task_1/null-shot/gpt_4o" -data_type "json" -pe_type "task_1/null-shot" -llm "gpt-4o-2024-08-06" -temperature 0
python ./src/response_gathering.py -source "./data/task_1/" -destination "./responses/task_1/null-shot/gpt_4o" -data_type "image" -pe_type "task_1/null-shot" -llm "gpt-4o-2024-08-06" -temperature 0

python ./src/response_gathering.py -source "./data/task_1/" -destination "./responses/task_1/null-shot-cot/gpt_4o" -data_type "xml" -pe_type "task_1/null-shot-cot" -llm "gpt-4o-2024-08-06" -temperature 0
python ./src/response_gathering.py -source "./data/task_1/" -destination "./responses/task_1/null-shot-cot/gpt_4o" -data_type "json" -pe_type "task_1/null-shot-cot" -llm "gpt-4o-2024-08-06" -temperature 0
python ./src/response_gathering.py -source "./data/task_1/" -destination "./responses/task_1/null-shot-cot/gpt_4o" -data_type "image" -pe_type "task_1/null-shot-cot" -llm "gpt-4o-2024-08-06" -temperature 0


python ./src/response_gathering.py -source "./data/task_1/" -destination "./responses/task_1/zero-shot/gpt_4-1-mini" -data_type "xml" -pe_type "task_1/zero-shot" -llm "gpt-4.1-mini-2025-04-14" -temperature 0
python ./src/response_gathering.py -source "./data/task_1/" -destination "./responses/task_1/zero-shot/gpt_4-1-mini" -data_type "json" -pe_type "task_1/zero-shot" -llm "gpt-4.1-mini-2025-04-14" -temperature 0
python ./src/response_gathering.py -source "./data/task_1/" -destination "./responses/task_1/zero-shot/gpt_4-1-mini" -data_type "image" -pe_type "task_1/zero-shot" -llm "gpt-4.1-mini-2025-04-14" -temperature 0

python ./src/response_gathering.py -source "./data/task_1/" -destination "./responses/task_1/zero-shot-cot/gpt_4-1-mini" -data_type "xml" -pe_type "task_1/zero-shot-cot" -llm "gpt-4.1-mini-2025-04-14" -temperature 0
python ./src/response_gathering.py -source "./data/task_1/" -destination "./responses/task_1/zero-shot-cot/gpt_4-1-mini" -data_type "json" -pe_type "task_1/zero-shot-cot" -llm "gpt-4.1-mini-2025-04-14" -temperature 0
python ./src/response_gathering.py -source "./data/task_1/" -destination "./responses/task_1/zero-shot-cot/gpt_4-1-mini" -data_type "image" -pe_type "task_1/zero-shot-cot" -llm "gpt-4.1-mini-2025-04-14" -temperature 0

python ./src/response_gathering.py -source "./data/task_1/" -destination "./responses/task_1/null-shot/gpt_4-1-mini" -data_type "xml" -pe_type "task_1/null-shot" -llm "gpt-4.1-mini-2025-04-14" -temperature 0
python ./src/response_gathering.py -source "./data/task_1/" -destination "./responses/task_1/null-shot/gpt_4-1-mini" -data_type "json" -pe_type "task_1/null-shot" -llm "gpt-4.1-mini-2025-04-14" -temperature 0
python ./src/response_gathering.py -source "./data/task_1/" -destination "./responses/task_1/null-shot/gpt_4-1-mini" -data_type "image" -pe_type "task_1/null-shot" -llm "gpt-4.1-mini-2025-04-14" -temperature 0

python ./src/response_gathering.py -source "./data/task_1/" -destination "./responses/task_1/null-shot-cot/gpt_4-1-mini" -data_type "xml" -pe_type "task_1/null-shot-cot" -llm "gpt-4.1-mini-2025-04-14" -temperature 0
python ./src/response_gathering.py -source "./data/task_1/" -destination "./responses/task_1/null-shot-cot/gpt_4-1-mini" -data_type "json" -pe_type "task_1/null-shot-cot" -llm "gpt-4.1-mini-2025-04-14" -temperature 0
python ./src/response_gathering.py -source "./data/task_1/" -destination "./responses/task_1/null-shot-cot/gpt_4-1-mini" -data_type "image" -pe_type "task_1/null-shot-cot" -llm "gpt-4.1-mini-2025-04-14" -temperature 0

