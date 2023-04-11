import os
import openai
from human_eval.data import write_jsonl, read_problems

# openai.api_base = "http://openaigw.uk/v1/"
openai.api_base = "https://api.openai.com/v1"
openai.api_key = os.getenv("OPENAI_API_KEY")
# m = "code-davinci-002"
m = "text-davinci-003"

def generate_openai_completion(p):
    print(p)
    response = openai.Completion.create(
        model=m,
        prompt=p,
        temperature=0,
        max_tokens=64,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    print(response.choices[0])
    return response.choices[0].text

problems = read_problems()

# num_samples_per_task = 200
samples = []
for task_id, task in problems.items():
    samples.append(dict(task_id=task_id, completion=generate_openai_completion(task["prompt"])))

# samples = [
#     dict(task_id=task_id, completion=generate_openai_completion(problems[task_id]["prompt"]))
#     for task_id in problems
#     for _ in range(num_samples_per_task)
# ]
write_jsonl("data/openai.jsonl", samples)

# print(generate_openai_completion("def return1():\n"))