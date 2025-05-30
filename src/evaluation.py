import statistics
import argparse
import json
import scipy.stats as stats
from pathlib import Path
from utils import file_manager as fm
import re
from collections import Counter

def extract_answer(filepath, task_num):
    try:
        j_str = fm.read_json(filepath)
        
        # First try to get the raw response content
        if '_response' in j_str:
            raw_response = j_str['_response']
        else:
            raw_response = j_str.get('response', '')
        
        # Case 1: Response is a string containing JSON
        if isinstance(raw_response, str):
            try:
                # Remove potential trailing garbage (like in the second anomaly example)
                cleaned_response = raw_response.split('}')[0] + '}'  # Simple cleanup
                j_response = json.loads(cleaned_response)
                answer_str = j_response.get('answer', '').lower()
            except (json.JSONDecodeError, AttributeError):
                # If parsing fails, try to extract answer directly from string
                match = re.search(r'"answer"\s*:\s*"([a-d])"', raw_response, re.IGNORECASE)
                if match:
                    answer_str = match.group(1).lower()
                else:
                    return "invalid"
        
        # Case 2: Response is already a dict
        elif isinstance(raw_response, dict):
            if raw_response.get('answer') is None:
                return "invalid"
            answer_str = raw_response['answer'].lower()
        else:
            return "invalid"
        
        # Now process the answer string
        if not answer_str:  # Empty answer
            return "invalid"
            
        if task_num == 1:    
            return answer_str == 'true' or answer_str == 'stable'
        elif task_num == 2 or task_num == 3:
            # Extract answer letter from various patterns
            match = re.search(
                r'(?:structure|image|labeled|answer is|choose|select)\s*(?:is|in|:|")?\s*[\'"]?([a-d])[\'"]?', 
                answer_str, 
                re.IGNORECASE
            )
            if match:
                return match.group(1).lower()
            # Fallback: look for standalone letters
            match = re.search(r'\b([a-d])\b', answer_str, re.IGNORECASE)
            if match:
                return match.group(1).lower()
            return "invalid"
        else:
            return answer_str == 'true' or answer_str == 'stable'
        
    except Exception as e:
        print(f"Error processing {filepath}: {str(e)}")
        return "invalid"

def get_gt(filepath, task_num):
    try:
        if  task_num==1:
            if 'unstable' in filepath.stem.lower():
                return False
            elif 'stable' in filepath.stem.lower():
                return True
        elif task_num==2 or task_num==3:
            return filepath.stem.split('_')[-1].lower()
        else:
            return False
            #return filepath.stem.lower().startswith('stable')
    except:
        return None

def binomial_test(answers:list):
    expected_proportion=0.5
    alpha=0.0001
    true_ans=len([a for a in answers if a==True])
    n=len(answers)
    result = stats.binomtest(true_ans, n, expected_proportion, alternative='two-sided')
    if result.pvalue < alpha:
        if true_ans>=0.5:
            bias=100*true_ans/n
            msg=f"Reject the null hypothesis: The proportion significantly deviates towards TRUE (proportion: {bias}%, p:{result.pvalue})."
        else:
            bias=100*(n-true_ans)/n
            msg=f"Reject the null hypothesis: The proportion significantly deviates towards FALSE (proportion: {bias}%, p:{result.pvalue})."
        print(msg)
    else:
        msg=f"Fail to reject the null hypothesis: No significant deviation from the expected value (p:{result.pvalue})."
        print(msg)
    return result.pvalue, msg

def chi_square_test(answers: list, alpha: float = 0.0001):
    """
    Test whether the answers are biased towards 'C' using chi-square test.
    Returns the p-value and a message.
    """
    filtered_answers = [a for a in answers if a is not None]
    counts = Counter(filtered_answers)
    choices = sorted(counts.keys())
    observed = [counts[choice] for choice in choices]
    n = sum(observed)
    if n == 0:
        return None, "No valid answers to test."
    expected = [n / len(choices)] * len(choices)  # Equal probability for each answer
    print(f"Observed: {observed}, Expected: {expected}")
    # Perform the chi-square test
    chi2, p = stats.chisquare(f_obs=observed, f_exp=expected)
    if p < alpha:
        msg = f"Reject the null hypothesis: The distribution is significantly biased (p: {p})."
        max_choice = choices[observed.index(max(observed))]
        max_prop = max(observed) / n
        msg += f" Most frequent answer: '{max_choice}' with proportion: {max_prop:.2%}."
    else:
        msg = f"Fail to reject the null hypothesis: No significant bias detected (p: {p})."
    print(msg)
    return p, msg

def get_task_number(source_dir:str)->int:
    task_number = 0
    if 'task_1' in source_dir:
        task_number = 1
    elif 'task_2' in source_dir:
        task_number = 2
    elif 'task_3' in source_dir:
        task_number = 3
    return task_number

def evaluate(source_dir:str, target_dir:str):
    csv_header=['no', 'file', 'gt', 'answer', 'score']
    s_dir=Path(source_dir)
    t_dir=Path(target_dir)
    tn =get_task_number(source_dir)
    
    directories=[d for d in s_dir.iterdir() if d.is_dir()]
    #print(f"Directories: {directories}")
    
    for dir in directories:
        files=[f for f in dir.iterdir() if f.is_file()]
        rows=[]
        answers=[]
        scores=[]
        for i, file in enumerate(files):
            gt=get_gt(file, tn)
            t_ans=extract_answer(file, tn)
            
            if t_ans is not None:
                t_score= 1 if t_ans==gt else 0
            else:
                t_score=0
            answers.append(t_ans)
            scores.append(t_score)
            
            t_row=[i+1, str(file), gt, t_ans, t_score]
            rows.append(t_row)
        
        mean=statistics.mean(scores)
        rows.append(['mean', mean, '', '', ''])
        
        #pval, msg=binomial_test(answers=answers)
        #pval, msg=chi_square_test(answers=answers)
        #rows.append(['binomial_test', 'p', pval, msg, ''])

        t_file=t_dir.joinpath(f'{dir.stem}.csv')
        fm.write_csv(path=t_file, data=rows, header=csv_header)
    pass

def main():
    arg_parser = argparse.ArgumentParser(prog="evaluation", description="evaluation")
    arg_parser.add_argument("-source", type=str, required=True)
    arg_parser.add_argument("-destination", type=str, required=True)
    args = arg_parser.parse_args()
    evaluate(source_dir=args.source, target_dir=args.destination)
    pass

if __name__=="__main__":
    main()