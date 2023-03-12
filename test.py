import os
import openai
from human_eval.data import write_jsonl, read_problems

openai.api_base = "http://openaigw.uk/v1/"
openai.api_key = os.getenv("OPENAI_API_KEY")
m = "code-davinci-002"
# m = "text-davinci-003"

# models = openai.Model.list()
# print(models.data[0].id)
# p = "from typing import List\n\n\ndef has_close_elements(numbers: List[float], threshold: float) -> bool:\n    \"\"\" Check if in given list of numbers, are any two numbers closer to each other than\n    given threshold.\n    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)\n    False\n    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)\n    True\n    \"\"\"\n"
def generate_openai_completion(p):
    response = openai.Completion.create(
        model=m,
        prompt=p,
        temperature=0,
        max_tokens=3,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    print(response.choices[0])
    return response.choices[0].text

problems = read_problems()

num_samples_per_task = 200
samples = [
    dict(task_id=task_id, completion=generate_openai_completion(problems[task_id]["prompt"]))
    for task_id in problems
    for _ in range(num_samples_per_task)
]
write_jsonl("data/openai.jsonl", samples)

# print(generate_openai_completion("def return1():\n"))