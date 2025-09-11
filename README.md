# game-physics-eval

This repository contains tools and data for evaluating MLLM responses in game physics tasks.

## 📄 Publications

### **1. IEEE COG 2025 Conference Paper** ✅ *(Published)*
**Title:** *Can Multimodal LLMs Reason About Stability? An Exploratory Study with Insights from the LLMs4PCG Challenge*  
**Link:** [https://ieeexplore.ieee.org/document/11114183/](https://ieeexplore.ieee.org/document/11114183/)  
**Tag:** `cog-2025-published`


## 📦 Repository Contents

- **`src/response_gathering_(Task).py`**  
  Script to gather model responses for a specified task.

- **`scripts/gathering_response.sh`**  
  A shell wrapper to run response gathering across *all* data types and models in one go.

- **`requirements.txt`**  
  Python dependencies needed for running the scripts.

---

## 🔗 Data Sources

- **Dataset generator**  
  https://github.com/anonymouspenguin27/game-physics-benchmark
  
- **Raw results from MLLM responses**  
  Located on Hugging Face:  
  https://huggingface.co/datasets/FajarD/game-physics-eval/tree/main

---

## 🚀 Usage

### 1. Setup environment

Install required packages:

```bash
pip install -r requirements.txt
```
### 2. Gather responses for a specific task

Run the Python script with arguments:

```
python src/response_gathering_<Task>.py \
  -source <data> \
  -destination <output_directory> \
  -data_type <data_type> \
  -pe_type <prompt_directory> \
  -llm <model_name> \
  -temperature <temperature>
```

Arguments:

- source: Path or identifier of the input dataset

- destination: Directory to save the gathered responses

- data_type: Data category (e.g., questions, prompts)

- pe_type: Prompt engineering directory type

- llm: Model identifier to generate responses (e.g., gpt-4, vicuna-13b)

- temperature: Sampling temperature (e.g., 0.7, 1.0)

### 3. Gather all responses
To collect responses across all data types and models:

```bash
bash scripts/gathering_response.sh
```

📁 Directory Structure

```
.
├── README.md
├── requirements.txt
├── src/
│   └── response_gathering_<Task>.py
└── scripts/
    └── gathering_response.sh
```

## 📊 Comparison with Existing Work
| Dataset  | Size / Levels     | Model Type  | Game Environment | Modality          | Target Task                                                                         |
| -------- | ----------------- | ----------- | ---------------- | ----------------- | ----------------------------------------------------------------------------------- |
| **Ours** | 300 levels        | Multimodal  | ✅ Yes            | XML, JSON, Image  | Physical reasoning, specifically stability, in visually grounded game contexts      |
| Newton   | 160k QA questions | LLM         | ❌ No             | Text              | Physics reasoning skills on everyday object attributes                              |
| Phyx     | 3K questions      | Multimodal  | ❌ No             | Image and Text    | Physics-grounded reasoning across 6 core physics domains                            |
| Phyre    | 5,000 tasks       | Traditional | ✅ Yes            | Visual            | Physical reasoning and generalization in 2D classical mechanics puzzles             |
| NovPhy   | 40 task templates | Traditional | ✅ Yes            | Visual + Symbolic | Physical reasoning with novelty detection and adaptation in open-world environments |
