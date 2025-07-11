# Statistical test

## Task 1

|model        |pe_type      |modality|mean_score|p_value|significant           |
|-------------|-------------|--------|----------|-------|----------------------|
|gemma3-4b    |null-shot    |image   |0.54      |1.662e-01|No                    |
|gemma3-4b    |null-shot    |json    |0.46      |2.045e-01|No                    |
|gemma3-4b    |null-shot    |xml     |0.51      |6.449e-01|No                    |
|gemma3-4b    |null-shot-cot|image   |0.53      |2.995e-01|No                    |
|gemma3-4b    |null-shot-cot|json    |0.57      |1.507e-02|Yes                   |
|gemma3-4b    |null-shot-cot|xml     |0.55      |1.061e-01|No                    |
|gemma3-4b    |zero-shot    |image   |0.55      |8.326e-02|No                    |
|gemma3-4b    |zero-shot    |json    |0.56      |3.745e-02|Yes                   |
|gemma3-4b    |zero-shot    |xml     |0.57      |1.507e-02|Yes                   |
|gemma3-4b    |zero-shot-cot|image   |0.51      |8.178e-01|No                    |
|gemma3-4b    |zero-shot-cot|json    |0.51      |7.297e-01|No                    |
|gemma3-4b    |zero-shot-cot|xml     |0.55      |1.061e-01|No                    |
|gpt_4-1-mini |null-shot    |image   |0.55      |1.061e-01|No                    |
|gpt_4-1-mini |null-shot    |json    |0.52      |5.646e-01|No                    |
|gpt_4-1-mini |null-shot    |xml     |0.53      |2.995e-01|No                    |
|gpt_4-1-mini |null-shot-cot|image   |0.55      |8.326e-02|No                    |
|gpt_4-1-mini |null-shot-cot|json    |0.56      |3.745e-02|Yes                   |
|gpt_4-1-mini |null-shot-cot|xml     |0.54      |1.662e-01|No                    |
|gpt_4-1-mini |zero-shot    |image   |0.58      |5.398e-03|Yes                   |
|gpt_4-1-mini |zero-shot    |json    |0.51      |7.297e-01|No                    |
|gpt_4-1-mini |zero-shot    |xml     |0.5       |9.083e-01|No                    |
|gpt_4-1-mini |zero-shot-cot|image   |0.59      |1.715e-03|Yes                   |
|gpt_4-1-mini |zero-shot-cot|json    |0.55      |1.061e-01|No                    |
|gpt_4-1-mini |zero-shot-cot|xml     |0.55      |1.061e-01|No                    |
|gpt_4o       |null-shot    |image   |0.65      |2.190e-07|Yes                   |
|gpt_4o       |null-shot    |json    |0.5       |1.000e+00|No                    |
|gpt_4o       |null-shot    |xml     |0.5       |9.083e-01|No                    |
|gpt_4o       |null-shot-cot|image   |0.65      |1.121e-07|Yes                   |
|gpt_4o       |null-shot-cot|json    |0.48      |5.646e-01|No                    |
|gpt_4o       |null-shot-cot|xml     |0.52      |5.646e-01|No                    |
|gpt_4o       |zero-shot    |image   |0.64      |4.207e-07|Yes                   |
|gpt_4o       |zero-shot    |json    |0.49      |8.178e-01|No                    |
|gpt_4o       |zero-shot    |xml     |0.48      |5.646e-01|No                    |
|gpt_4o       |zero-shot-cot|image   |0.62      |1.499e-05|Yes                   |
|gpt_4o       |zero-shot-cot|json    |0.49      |6.449e-01|No                    |
|gpt_4o       |zero-shot-cot|xml     |0.51      |6.449e-01|No                    |
|llava-7b     |null-shot    |image   |0.5       |1.000e+00|No                    |
|llava-7b     |null-shot    |json    |0.54      |2.045e-01|No                    |
|llava-7b     |null-shot    |xml     |0.45      |8.326e-02|No                    |
|llava-7b     |null-shot-cot|image   |0.5       |1.000e+00|No                    |
|llava-7b     |null-shot-cot|json    |0.54      |2.045e-01|No                    |
|llava-7b     |null-shot-cot|xml     |0.56      |3.745e-02|Yes                   |
|llava-7b     |zero-shot    |image   |0.5       |9.083e-01|No                    |
|llava-7b     |zero-shot    |json    |0.51      |7.297e-01|No                    |
|llava-7b     |zero-shot    |xml     |0.51      |7.297e-01|No                    |
|llava-7b     |zero-shot-cot|image   |0.5       |1.000e+00|No                    |
|llava-7b     |zero-shot-cot|json    |0.48      |5.646e-01|No                    |
|llava-7b     |zero-shot-cot|xml     |0.51      |8.178e-01|No                    |
|qwen2.5-vl-3b|null-shot    |image   |0.5       |9.083e-01|No                    |
|qwen2.5-vl-3b|null-shot    |json    |0.49      |7.297e-01|No                    |
|qwen2.5-vl-3b|null-shot    |xml     |0.5       |1.000e+00|No                    |
|qwen2.5-vl-3b|null-shot-cot|image   |0.49      |7.297e-01|No                    |
|qwen2.5-vl-3b|null-shot-cot|json    |0.48      |5.646e-01|No                    |
|qwen2.5-vl-3b|null-shot-cot|xml     |0.5       |9.083e-01|No                    |
|qwen2.5-vl-3b|zero-shot    |image   |0.49      |7.297e-01|No                    |
|qwen2.5-vl-3b|zero-shot    |json    |0.52      |5.646e-01|No                    |
|qwen2.5-vl-3b|zero-shot    |xml     |0.51      |6.449e-01|No                    |
|qwen2.5-vl-3b|zero-shot-cot|image   |0.48      |4.893e-01|No                    |
|qwen2.5-vl-3b|zero-shot-cot|json    |0.51      |6.449e-01|No                    |
|qwen2.5-vl-3b|zero-shot-cot|xml     |0.52      |4.198e-01|No                    |
|qwen2.5-vl-7b|null-shot    |image   |0.48      |5.646e-01|No                    |
|qwen2.5-vl-7b|null-shot    |json    |0.5       |1.000e+00|No                    |
|qwen2.5-vl-7b|null-shot    |xml     |0.45      |8.326e-02|No                    |
|qwen2.5-vl-7b|null-shot-cot|image   |0.46      |1.336e-01|No                    |
|qwen2.5-vl-7b|null-shot-cot|json    |0.5       |9.083e-01|No                    |
|qwen2.5-vl-7b|null-shot-cot|xml     |0.54      |1.662e-01|No                    |
|qwen2.5-vl-7b|zero-shot    |image   |0.51      |6.449e-01|No                    |
|qwen2.5-vl-7b|zero-shot    |json    |0.46      |2.045e-01|No                    |
|qwen2.5-vl-7b|zero-shot    |xml     |0.53      |2.995e-01|No                    |
|qwen2.5-vl-7b|zero-shot-cot|image   |0.54      |1.336e-01|No                    |
|qwen2.5-vl-7b|zero-shot-cot|json    |0.51      |7.297e-01|No                    |
|qwen2.5-vl-7b|zero-shot-cot|xml     |0.49      |8.178e-01|No                    |



## Task 2

|model        |pe_type      |modality|number_of_option|mean_score|p_value               |significant|
|-------------|-------------|--------|----------------|----------|----------------------|-----------|
|gemma3-4b    |null-shot    |image   |2               |0.41      |7.167e-02             |No         |
|gemma3-4b    |null-shot    |json    |2               |0.32      |2.176e-04             |Yes        |
|gemma3-4b    |null-shot    |xml     |2               |0.38      |1.563e-02             |Yes        |
|gpt_4-1-mini |null-shot    |image   |2               |0.66      |1.106e-03             |Yes        |
|gpt_4-1-mini |null-shot    |json    |2               |0.47      |5.512e-01             |No         |
|gpt_4-1-mini |null-shot    |xml     |2               |0.46      |4.265e-01             |No         |
|gpt_4o       |null-shot    |image   |2               |0.73      |1.301e-06             |Yes        |
|gpt_4o       |null-shot    |json    |2               |0.45      |3.197e-01             |No         |
|gpt_4o       |null-shot    |xml     |2               |0.48      |6.913e-01             |No         |
|llava-7b     |null-shot    |image   |2               |0.22      |1.139e-09             |Yes        |
|llava-7b     |null-shot    |json    |2               |0.25      |1.017e-07             |Yes        |
|llava-7b     |null-shot    |xml     |2               |0.25      |1.017e-07             |Yes        |
|qwen2.5-vl-3b|null-shot    |image   |2               |0.21      |2.069e-10             |Yes        |
|qwen2.5-vl-3b|null-shot    |json    |2               |0.35      |2.304e-03             |Yes        |
|qwen2.5-vl-3b|null-shot    |xml     |2               |0.4       |4.493e-02             |Yes        |
|qwen2.5-vl-7b|null-shot    |image   |2               |0.43      |1.626e-01             |No         |
|qwen2.5-vl-7b|null-shot    |json    |2               |0.29      |1.229e-05             |Yes        |
|qwen2.5-vl-7b|null-shot    |xml     |2               |0.4       |4.493e-02             |Yes        |
|gemma3-4b    |null-shot-cot|image   |2               |0.39      |2.706e-02             |Yes        |
|gemma3-4b    |null-shot-cot|json    |2               |0.31      |8.873e-05             |Yes        |
|gemma3-4b    |null-shot-cot|xml     |2               |0.34      |1.106e-03             |Yes        |
|gpt_4-1-mini |null-shot-cot|image   |2               |0.74      |3.789e-07             |Yes        |
|gpt_4-1-mini |null-shot-cot|json    |2               |0.48      |6.913e-01             |No         |
|gpt_4-1-mini |null-shot-cot|xml     |2               |0.48      |6.913e-01             |No         |
|gpt_4o       |null-shot-cot|image   |2               |0.75      |1.017e-07             |Yes        |
|gpt_4o       |null-shot-cot|json    |2               |0.46      |4.265e-01             |No         |
|gpt_4o       |null-shot-cot|xml     |2               |0.49      |8.426e-01             |No         |
|llava-7b     |null-shot-cot|image   |2               |0.24      |2.505e-08             |Yes        |
|llava-7b     |null-shot-cot|json    |2               |0.25      |1.017e-07             |Yes        |
|llava-7b     |null-shot-cot|xml     |2               |0.22      |1.139e-09             |Yes        |
|qwen2.5-vl-3b|null-shot-cot|image   |2               |0.29      |1.229e-05             |Yes        |
|qwen2.5-vl-3b|null-shot-cot|json    |2               |0.41      |7.167e-02             |No         |
|qwen2.5-vl-3b|null-shot-cot|xml     |2               |0.37      |8.645e-03             |Yes        |
|qwen2.5-vl-7b|null-shot-cot|image   |2               |0.42      |1.100e-01             |No         |
|qwen2.5-vl-7b|null-shot-cot|json    |2               |0.36      |4.570e-03             |Yes        |
|qwen2.5-vl-7b|null-shot-cot|xml     |2               |0.38      |1.563e-02             |Yes        |
|gemma3-4b    |zero-shot    |image   |2               |0.44      |2.320e-01             |No         |
|gemma3-4b    |zero-shot    |json    |2               |0.34      |1.106e-03             |Yes        |
|gemma3-4b    |zero-shot    |xml     |2               |0.42      |1.100e-01             |No         |
|gpt_4-1-mini |zero-shot    |image   |2               |0.75      |1.017e-07             |Yes        |
|gpt_4-1-mini |zero-shot    |json    |2               |0.47      |5.512e-01             |No         |
|gpt_4-1-mini |zero-shot    |xml     |2               |0.41      |7.167e-02             |No         |
|gpt_4o       |zero-shot    |image   |2               |0.76      |2.505e-08             |Yes        |
|gpt_4o       |zero-shot    |json    |2               |0.49      |8.426e-01             |No         |
|gpt_4o       |zero-shot    |xml     |2               |0.48      |6.913e-01             |No         |
|llava-7b     |zero-shot    |image   |2               |0.24      |2.505e-08             |Yes        |
|llava-7b     |zero-shot    |json    |2               |0.35      |2.304e-03             |Yes        |
|llava-7b     |zero-shot    |xml     |2               |0.29      |1.229e-05             |Yes        |
|qwen2.5-vl-3b|zero-shot    |image   |2               |0.31      |8.873e-05             |Yes        |
|qwen2.5-vl-3b|zero-shot    |json    |2               |0.46      |4.265e-01             |No         |
|qwen2.5-vl-3b|zero-shot    |xml     |2               |0.42      |1.100e-01             |No         |
|qwen2.5-vl-7b|zero-shot    |image   |2               |0.43      |1.626e-01             |No         |
|qwen2.5-vl-7b|zero-shot    |json    |2               |0.37      |8.645e-03             |Yes        |
|qwen2.5-vl-7b|zero-shot    |xml     |2               |0.39      |2.706e-02             |Yes        |
|gemma3-4b    |zero-shot-cot|image   |2               |0.43      |1.626e-01             |No         |
|gemma3-4b    |zero-shot-cot|json    |2               |0.25      |1.017e-07             |Yes        |
|gemma3-4b    |zero-shot-cot|xml     |2               |0.44      |2.320e-01             |No         |
|gpt_4-1-mini |zero-shot-cot|image   |2               |0.74      |3.789e-07             |Yes        |
|gpt_4-1-mini |zero-shot-cot|json    |2               |0.6       |4.493e-02             |Yes        |
|gpt_4-1-mini |zero-shot-cot|xml     |2               |0.55      |3.197e-01             |No         |
|gpt_4o       |zero-shot-cot|image   |2               |0.73      |1.301e-06             |Yes        |
|gpt_4o       |zero-shot-cot|json    |2               |0.46      |4.265e-01             |No         |
|gpt_4o       |zero-shot-cot|xml     |2               |0.5       |1.000e+00             |No         |
|llava-7b     |zero-shot-cot|image   |2               |0.24      |2.505e-08             |Yes        |
|llava-7b     |zero-shot-cot|json    |2               |0.31      |8.873e-05             |Yes        |
|llava-7b     |zero-shot-cot|xml     |2               |0.32      |2.176e-04             |Yes        |
|qwen2.5-vl-3b|zero-shot-cot|image   |2               |0.36      |4.570e-03             |Yes        |
|qwen2.5-vl-3b|zero-shot-cot|json    |2               |0.46      |4.265e-01             |No         |
|qwen2.5-vl-3b|zero-shot-cot|xml     |2               |0.38      |1.563e-02             |Yes        |
|qwen2.5-vl-7b|zero-shot-cot|image   |2               |0.46      |4.265e-01             |No         |
|qwen2.5-vl-7b|zero-shot-cot|json    |2               |0.35      |2.304e-03             |Yes        |
|qwen2.5-vl-7b|zero-shot-cot|xml     |2               |0.44      |2.320e-01             |No         |
|gemma3-4b    |null-shot    |image   |3               |0.44      |3.497e-02             |Yes        |
|gemma3-4b    |null-shot    |json    |3               |0.26      |9.938e-02             |No         |
|gemma3-4b    |null-shot    |xml     |3               |0.35      |7.288e-01             |No         |
|gpt_4-1-mini |null-shot    |image   |3               |0.52      |3.334e-04             |Yes        |
|gpt_4-1-mini |null-shot    |json    |3               |0.44      |3.497e-02             |Yes        |
|gpt_4-1-mini |null-shot    |xml     |3               |0.41      |1.241e-01             |No         |
|gpt_4o       |null-shot    |image   |3               |0.66      |5.987e-10             |Yes        |
|gpt_4o       |null-shot    |json    |3               |0.54      |7.703e-05             |Yes        |
|gpt_4o       |null-shot    |xml     |3               |0.49      |2.382e-03             |Yes        |
|llava-7b     |null-shot    |image   |3               |0.15      |1.579e-06             |Yes        |
|llava-7b     |null-shot    |json    |3               |0.32      |7.767e-01             |No         |
|llava-7b     |null-shot    |xml     |3               |0.38      |3.411e-01             |No         |
|qwen2.5-vl-3b|null-shot    |image   |3               |0.32      |7.767e-01             |No         |
|qwen2.5-vl-3b|null-shot    |json    |3               |0.35      |7.288e-01             |No         |
|qwen2.5-vl-3b|null-shot    |xml     |3               |0.43      |5.488e-02             |No         |
|qwen2.5-vl-7b|null-shot    |image   |3               |0.39      |2.505e-01             |No         |
|qwen2.5-vl-7b|null-shot    |json    |3               |0.37      |4.517e-01             |No         |
|qwen2.5-vl-7b|null-shot    |xml     |3               |0.36      |5.817e-01             |No         |
|gemma3-4b    |null-shot-cot|image   |3               |0.42      |8.371e-02             |No         |
|gemma3-4b    |null-shot-cot|json    |3               |0.26      |9.938e-02             |No         |
|gemma3-4b    |null-shot-cot|xml     |3               |0.34      |8.889e-01             |No         |
|gpt_4-1-mini |null-shot-cot|image   |3               |0.53      |1.628e-04             |Yes        |
|gpt_4-1-mini |null-shot-cot|json    |3               |0.45      |2.165e-02             |Yes        |
|gpt_4-1-mini |null-shot-cot|xml     |3               |0.41      |1.241e-01             |No         |
|gpt_4o       |null-shot-cot|image   |3               |0.64      |6.359e-09             |Yes        |
|gpt_4o       |null-shot-cot|json    |3               |0.54      |7.703e-05             |Yes        |
|gpt_4o       |null-shot-cot|xml     |3               |0.53      |1.628e-04             |Yes        |
|llava-7b     |null-shot-cot|image   |3               |0.16      |8.269e-06             |Yes        |
|llava-7b     |null-shot-cot|json    |3               |0.33      |9.439e-01             |No         |
|llava-7b     |null-shot-cot|xml     |3               |0.38      |3.411e-01             |No         |
|qwen2.5-vl-3b|null-shot-cot|image   |3               |0.39      |2.505e-01             |No         |
|qwen2.5-vl-3b|null-shot-cot|json    |3               |0.33      |9.439e-01             |No         |
|qwen2.5-vl-3b|null-shot-cot|xml     |3               |0.43      |5.488e-02             |No         |
|qwen2.5-vl-7b|null-shot-cot|image   |3               |0.46      |1.303e-02             |Yes        |
|qwen2.5-vl-7b|null-shot-cot|json    |3               |0.36      |5.817e-01             |No         |
|qwen2.5-vl-7b|null-shot-cot|xml     |3               |0.44      |3.497e-02             |Yes        |
|gemma3-4b    |zero-shot    |image   |3               |0.38      |3.411e-01             |No         |
|gemma3-4b    |zero-shot    |json    |3               |0.33      |9.439e-01             |No         |
|gemma3-4b    |zero-shot    |xml     |3               |0.33      |9.439e-01             |No         |
|gpt_4-1-mini |zero-shot    |image   |3               |0.43      |5.488e-02             |No         |
|gpt_4-1-mini |zero-shot    |json    |3               |0.4       |1.788e-01             |No         |
|gpt_4-1-mini |zero-shot    |xml     |3               |0.49      |2.382e-03             |Yes        |
|gpt_4o       |zero-shot    |image   |3               |0.65      |1.997e-09             |Yes        |
|gpt_4o       |zero-shot    |json    |3               |0.56      |1.565e-05             |Yes        |
|gpt_4o       |zero-shot    |xml     |3               |0.52      |3.334e-04             |Yes        |
|llava-7b     |zero-shot    |image   |3               |0.15      |1.579e-06             |Yes        |
|llava-7b     |zero-shot    |json    |3               |0.37      |4.517e-01             |No         |
|llava-7b     |zero-shot    |xml     |3               |0.37      |4.517e-01             |No         |
|qwen2.5-vl-3b|zero-shot    |image   |3               |0.38      |3.411e-01             |No         |
|qwen2.5-vl-3b|zero-shot    |json    |3               |0.35      |7.288e-01             |No         |
|qwen2.5-vl-3b|zero-shot    |xml     |3               |0.44      |3.497e-02             |Yes        |
|qwen2.5-vl-7b|zero-shot    |image   |3               |0.43      |5.488e-02             |No         |
|qwen2.5-vl-7b|zero-shot    |json    |3               |0.37      |4.517e-01             |No         |
|qwen2.5-vl-7b|zero-shot    |xml     |3               |0.38      |3.411e-01             |No         |
|gemma3-4b    |zero-shot-cot|image   |3               |0.35      |7.288e-01             |No         |
|gemma3-4b    |zero-shot-cot|json    |3               |0.29      |3.443e-01             |No         |
|gemma3-4b    |zero-shot-cot|xml     |3               |0.4       |1.788e-01             |No         |
|gpt_4-1-mini |zero-shot-cot|image   |3               |0.45      |2.165e-02             |Yes        |
|gpt_4-1-mini |zero-shot-cot|json    |3               |0.42      |8.371e-02             |No         |
|gpt_4-1-mini |zero-shot-cot|xml     |3               |0.44      |3.497e-02             |Yes        |
|gpt_4o       |zero-shot-cot|image   |3               |0.62      |5.659e-08             |Yes        |
|gpt_4o       |zero-shot-cot|json    |3               |0.51      |6.620e-04             |Yes        |
|gpt_4o       |zero-shot-cot|xml     |3               |0.45      |2.165e-02             |Yes        |
|llava-7b     |zero-shot-cot|image   |3               |0.18      |1.358e-04             |Yes        |
|llava-7b     |zero-shot-cot|json    |3               |0.29      |3.443e-01             |No         |
|llava-7b     |zero-shot-cot|xml     |3               |0.41      |1.241e-01             |No         |
|qwen2.5-vl-3b|zero-shot-cot|image   |3               |0.39      |2.505e-01             |No         |
|qwen2.5-vl-3b|zero-shot-cot|json    |3               |0.35      |7.288e-01             |No         |
|qwen2.5-vl-3b|zero-shot-cot|xml     |3               |0.41      |1.241e-01             |No         |
|qwen2.5-vl-7b|zero-shot-cot|image   |3               |0.42      |8.371e-02             |No         |
|qwen2.5-vl-7b|zero-shot-cot|json    |3               |0.41      |1.241e-01             |No         |
|qwen2.5-vl-7b|zero-shot-cot|xml     |3               |0.43      |5.488e-02             |No         |
|gemma3-4b    |null-shot    |image   |4               |0.36      |2.474e-02             |Yes        |
|gemma3-4b    |null-shot    |json    |4               |0.33      |9.363e-02             |No         |
|gemma3-4b    |null-shot    |xml     |4               |0.21      |3.309e-01             |No         |
|gpt_4-1-mini |null-shot    |image   |4               |0.63      |5.508e-12             |Yes        |
|gpt_4-1-mini |null-shot    |json    |4               |0.46      |6.013e-05             |Yes        |
|gpt_4-1-mini |null-shot    |xml     |4               |0.38      |8.994e-03             |Yes        |
|gpt_4o       |null-shot    |image   |4               |0.75      |6.405e-20             |Yes        |
|gpt_4o       |null-shot    |json    |4               |0.52      |5.054e-07             |Yes        |
|gpt_4o       |null-shot    |xml     |4               |0.44      |2.427e-04             |Yes        |
|llava-7b     |null-shot    |image   |4               |0.2       |2.165e-01             |No         |
|llava-7b     |null-shot    |json    |4               |0.39      |5.229e-03             |Yes        |
|llava-7b     |null-shot    |xml     |4               |0.41      |1.645e-03             |Yes        |
|qwen2.5-vl-3b|null-shot    |image   |4               |0.38      |8.994e-03             |Yes        |
|qwen2.5-vl-3b|null-shot    |json    |4               |0.34      |6.163e-02             |No         |
|qwen2.5-vl-3b|null-shot    |xml     |4               |0.32      |1.386e-01             |No         |
|qwen2.5-vl-7b|null-shot    |image   |4               |0.34      |6.163e-02             |No         |
|qwen2.5-vl-7b|null-shot    |json    |4               |0.37      |1.510e-02             |Yes        |
|qwen2.5-vl-7b|null-shot    |xml     |4               |0.34      |6.163e-02             |No         |
|gemma3-4b    |null-shot-cot|image   |4               |0.34      |6.163e-02             |No         |
|gemma3-4b    |null-shot-cot|json    |4               |0.35      |3.954e-02             |Yes        |
|gemma3-4b    |null-shot-cot|xml     |4               |0.29      |3.826e-01             |No         |
|gpt_4-1-mini |null-shot-cot|image   |4               |0.64      |1.583e-12             |Yes        |
|gpt_4-1-mini |null-shot-cot|json    |4               |0.48      |1.352e-05             |Yes        |
|gpt_4-1-mini |null-shot-cot|xml     |4               |0.4       |2.968e-03             |Yes        |
|gpt_4o       |null-shot-cot|image   |4               |0.74      |4.114e-19             |Yes        |
|gpt_4o       |null-shot-cot|json    |4               |0.46      |6.013e-05             |Yes        |
|gpt_4o       |null-shot-cot|xml     |4               |0.44      |2.427e-04             |Yes        |
|llava-7b     |null-shot-cot|image   |4               |0.21      |3.309e-01             |No         |
|llava-7b     |null-shot-cot|json    |4               |0.4       |2.968e-03             |Yes        |
|llava-7b     |null-shot-cot|xml     |4               |0.37      |1.510e-02             |Yes        |
|qwen2.5-vl-3b|null-shot-cot|image   |4               |0.38      |8.994e-03             |Yes        |
|qwen2.5-vl-3b|null-shot-cot|json    |4               |0.33      |9.363e-02             |No         |
|qwen2.5-vl-3b|null-shot-cot|xml     |4               |0.34      |6.163e-02             |No         |
|qwen2.5-vl-7b|null-shot-cot|image   |4               |0.31      |1.998e-01             |No         |
|qwen2.5-vl-7b|null-shot-cot|json    |4               |0.34      |6.163e-02             |No         |
|qwen2.5-vl-7b|null-shot-cot|xml     |4               |0.3       |2.803e-01             |No         |
|gemma3-4b    |zero-shot    |image   |4               |0.38      |8.994e-03             |Yes        |
|gemma3-4b    |zero-shot    |json    |4               |0.38      |8.994e-03             |Yes        |
|gemma3-4b    |zero-shot    |xml     |4               |0.33      |9.363e-02             |No         |
|gpt_4-1-mini |zero-shot    |image   |4               |0.6       |1.842e-10             |Yes        |
|gpt_4-1-mini |zero-shot    |json    |4               |0.36      |2.474e-02             |Yes        |
|gpt_4-1-mini |zero-shot    |xml     |4               |0.44      |2.427e-04             |Yes        |
|gpt_4o       |zero-shot    |image   |4               |0.74      |4.114e-19             |Yes        |
|gpt_4o       |zero-shot    |json    |4               |0.51      |1.195e-06             |Yes        |
|gpt_4o       |zero-shot    |xml     |4               |0.41      |1.645e-03             |Yes        |
|llava-7b     |zero-shot    |image   |4               |0.2       |2.165e-01             |No         |
|llava-7b     |zero-shot    |json    |4               |0.39      |5.229e-03             |Yes        |
|llava-7b     |zero-shot    |xml     |4               |0.35      |3.954e-02             |Yes        |
|qwen2.5-vl-3b|zero-shot    |image   |4               |0.33      |9.363e-02             |No         |
|qwen2.5-vl-3b|zero-shot    |json    |4               |0.33      |9.363e-02             |No         |
|qwen2.5-vl-3b|zero-shot    |xml     |4               |0.29      |3.826e-01             |No         |
|qwen2.5-vl-7b|zero-shot    |image   |4               |0.38      |8.994e-03             |Yes        |
|qwen2.5-vl-7b|zero-shot    |json    |4               |0.4       |2.968e-03             |Yes        |
|qwen2.5-vl-7b|zero-shot    |xml     |4               |0.32      |1.386e-01             |No         |
|gemma3-4b    |zero-shot-cot|image   |4               |0.4       |2.968e-03             |Yes        |
|gemma3-4b    |zero-shot-cot|json    |4               |0.37      |1.510e-02             |Yes        |
|gemma3-4b    |zero-shot-cot|xml     |4               |0.37      |1.510e-02             |Yes        |
|gpt_4-1-mini |zero-shot-cot|image   |4               |0.6       |1.842e-10             |Yes        |
|gpt_4-1-mini |zero-shot-cot|json    |4               |0.5       |2.752e-06             |Yes        |
|gpt_4-1-mini |zero-shot-cot|xml     |4               |0.43      |4.703e-04             |Yes        |
|gpt_4o       |zero-shot-cot|image   |4               |0.76      |9.193e-21             |Yes        |
|gpt_4o       |zero-shot-cot|json    |4               |0.49      |6.178e-06             |Yes        |
|gpt_4o       |zero-shot-cot|xml     |4               |0.48      |1.352e-05             |Yes        |
|llava-7b     |zero-shot-cot|image   |4               |0.27      |6.550e-01             |No         |
|llava-7b     |zero-shot-cot|json    |4               |0.37      |1.510e-02             |Yes        |
|llava-7b     |zero-shot-cot|xml     |4               |0.31      |1.998e-01             |No         |
|qwen2.5-vl-3b|zero-shot-cot|image   |4               |0.34      |6.163e-02             |No         |
|qwen2.5-vl-3b|zero-shot-cot|json    |4               |0.33      |9.363e-02             |No         |
|qwen2.5-vl-3b|zero-shot-cot|xml     |4               |0.24      |8.163e-01             |No         |
|qwen2.5-vl-7b|zero-shot-cot|image   |4               |0.32      |1.386e-01             |No         |
|qwen2.5-vl-7b|zero-shot-cot|json    |4               |0.36      |2.474e-02             |Yes        |
|qwen2.5-vl-7b|zero-shot-cot|xml     |4               |0.27      |6.550e-01             |No         |


## Task 3

|model        |pe_type      |modality|mean_score|p_value|significant           |
|-------------|-------------|--------|----------|-------|----------------------|
|gemma3-4b    |null-shot    |image   |0.2       |3.145e-02|Yes                   |
|gemma3-4b    |null-shot    |json    |0.18      |3.127e-03|Yes                   |
|gemma3-4b    |null-shot    |xml     |0.32      |1.376e-02|Yes                   |
|gemma3-4b    |null-shot-cot|image   |0.16      |1.267e-05|Yes                   |
|gemma3-4b    |null-shot-cot|json    |0.17      |5.319e-04|Yes                   |
|gemma3-4b    |null-shot-cot|xml     |0.33      |2.440e-03|Yes                   |
|gemma3-4b    |zero-shot    |image   |0.18      |1.795e-03|Yes                   |
|gemma3-4b    |zero-shot    |json    |0.14      |2.701e-07|Yes                   |
|gemma3-4b    |zero-shot    |xml     |0.31      |2.561e-02|Yes                   |
|gemma3-4b    |zero-shot-cot|image   |0.21      |6.522e-02|No                    |
|gemma3-4b    |zero-shot-cot|json    |0.19      |5.271e-03|Yes                   |
|gemma3-4b    |zero-shot-cot|xml     |0.32      |1.376e-02|Yes                   |
|gpt_4-1-mini |null-shot    |image   |0.44      |3.207e-10|Yes                   |
|gpt_4-1-mini |null-shot    |json    |0.7       |2.002e-46|Yes                   |
|gpt_4-1-mini |null-shot    |xml     |0.76      |2.330e-60|Yes                   |
|gpt_4-1-mini |null-shot-cot|image   |0.42      |7.253e-09|Yes                   |
|gpt_4-1-mini |null-shot-cot|json    |0.71      |8.192e-48|Yes                   |
|gpt_4-1-mini |null-shot-cot|xml     |0.78      |6.483e-65|Yes                   |
|gpt_4-1-mini |zero-shot    |image   |0.5       |3.308e-16|Yes                   |
|gpt_4-1-mini |zero-shot    |json    |0.73      |5.780e-53|Yes                   |
|gpt_4-1-mini |zero-shot    |xml     |0.83      |3.863e-81|Yes                   |
|gpt_4-1-mini |zero-shot-cot|image   |0.47      |3.330e-13|Yes                   |
|gpt_4-1-mini |zero-shot-cot|json    |0.68      |7.916e-42|Yes                   |
|gpt_4-1-mini |zero-shot-cot|xml     |0.81      |3.120e-75|Yes                   |
|gpt_4o       |null-shot    |image   |0.79      |7.930e-68|Yes                   |
|gpt_4o       |null-shot    |json    |0.62      |1.366e-31|Yes                   |
|gpt_4o       |null-shot    |xml     |0.64      |2.500e-35|Yes                   |
|gpt_4o       |null-shot-cot|image   |0.76      |1.243e-58|Yes                   |
|gpt_4o       |null-shot-cot|json    |0.64      |3.127e-34|Yes                   |
|gpt_4o       |null-shot-cot|xml     |0.65      |6.919e-36|Yes                   |
|gpt_4o       |zero-shot    |image   |0.76      |1.243e-58|Yes                   |
|gpt_4o       |zero-shot    |json    |0.66      |3.506e-38|Yes                   |
|gpt_4o       |zero-shot    |xml     |0.66      |1.344e-37|Yes                   |
|gpt_4o       |zero-shot-cot|image   |0.78      |5.644e-64|Yes                   |
|gpt_4o       |zero-shot-cot|json    |0.63      |1.084e-33|Yes                   |
|gpt_4o       |zero-shot-cot|xml     |0.61      |1.404e-29|Yes                   |
|llava-7b     |null-shot    |image   |0.22      |1.628e-01|No                    |
|llava-7b     |null-shot    |json    |0.2       |4.587e-02|Yes                   |
|llava-7b     |null-shot    |xml     |0.32      |1.376e-02|Yes                   |
|llava-7b     |null-shot-cot|image   |0.2       |2.100e-02|Yes                   |
|llava-7b     |null-shot-cot|json    |0.21      |1.228e-01|No                    |
|llava-7b     |null-shot-cot|xml     |0.3       |6.017e-02|No                    |
|llava-7b     |zero-shot    |image   |0.16      |6.429e-05|Yes                   |
|llava-7b     |zero-shot    |json    |0.19      |8.610e-03|Yes                   |
|llava-7b     |zero-shot    |xml     |0.39      |6.863e-07|Yes                   |
|llava-7b     |zero-shot-cot|image   |0.2       |3.145e-02|Yes                   |
|llava-7b     |zero-shot-cot|json    |0.2       |3.145e-02|Yes                   |
|llava-7b     |zero-shot-cot|xml     |0.4       |4.004e-07|Yes                   |
|qwen2.5-vl-3b|null-shot    |image   |0.21      |6.522e-02|No                    |
|qwen2.5-vl-3b|null-shot    |json    |0.22      |1.628e-01|No                    |
|qwen2.5-vl-3b|null-shot    |xml     |0.28      |3.035e-01|No                    |
|qwen2.5-vl-3b|null-shot-cot|image   |0.22      |2.691e-01|No                    |
|qwen2.5-vl-3b|null-shot-cot|json    |0.21      |6.522e-02|No                    |
|qwen2.5-vl-3b|null-shot-cot|xml     |0.32      |9.931e-03|Yes                   |
|qwen2.5-vl-3b|zero-shot    |image   |0.22      |2.691e-01|No                    |
|qwen2.5-vl-3b|zero-shot    |json    |0.22      |2.114e-01|No                    |
|qwen2.5-vl-3b|zero-shot    |xml     |0.3       |6.017e-02|No                    |
|qwen2.5-vl-3b|zero-shot-cot|image   |0.29      |1.285e-01|No                    |
|qwen2.5-vl-3b|zero-shot-cot|json    |0.21      |1.228e-01|No                    |
|qwen2.5-vl-3b|zero-shot-cot|xml     |0.3       |6.017e-02|No                    |
|qwen2.5-vl-7b|null-shot    |image   |0.25      |8.937e-01|No                    |
|qwen2.5-vl-7b|null-shot    |json    |0.18      |9.949e-04|Yes                   |
|qwen2.5-vl-7b|null-shot    |xml     |0.5       |1.469e-16|Yes                   |
|qwen2.5-vl-7b|null-shot-cot|image   |0.23      |4.962e-01|No                    |
|qwen2.5-vl-7b|null-shot-cot|json    |0.18      |9.949e-04|Yes                   |
|qwen2.5-vl-7b|null-shot-cot|xml     |0.47      |1.599e-13|Yes                   |
|qwen2.5-vl-7b|zero-shot    |image   |0.24      |7.884e-01|No                    |
|qwen2.5-vl-7b|zero-shot    |json    |0.18      |1.795e-03|Yes                   |
|qwen2.5-vl-7b|zero-shot    |xml     |0.52      |2.212e-18|Yes                   |
|qwen2.5-vl-7b|zero-shot-cot|image   |0.21      |9.052e-02|No                    |
|qwen2.5-vl-7b|zero-shot-cot|json    |0.17      |5.319e-04|Yes                   |
|qwen2.5-vl-7b|zero-shot-cot|xml     |0.53      |1.598e-19|Yes                   |

