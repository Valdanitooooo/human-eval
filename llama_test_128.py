import requests
import json
from human_eval.data import write_jsonl, read_problems


url = "http://xxxx:8013/generate"

def generate_llama_completion(p):
    print(p)
    params = {"max_length": 128, "prompt": p}
    data = json.dumps(params)
    print(data)
    res = requests.post(url=url, data=data)
    ret = res.json()
    print(ret)
    return ret.get('generated')[0]

problems = read_problems()

samples = []
for task_id, task in problems.items():
    samples.append(dict(task_id=task_id, completion=generate_llama_completion(task["prompt"])))

write_jsonl("data/llama13B_128.jsonl", samples)