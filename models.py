from google import genai
from google.genai.types import HttpOptions
import json
import re

with open("keys", "r") as f:
    api_key = f.readline()
    f.close()


def generate_framework(setup):
    prompt = (f"Create a {setup['framework']} RESTAPI with the following: \n"
              f"Endpoint: {setup['endpoint']}\n"
              f"Model fields: {setup['fields']}\n"
              f"Add operations(GET, POST). Add Swagger.")

    client = genai.Client(http_options=HttpOptions(api_version="v1"), api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=prompt,
    )
    print(response.text)
    return response.text


def parse_prompt(path="prompt"):
    with open(path, 'r') as f:
        lines = f.readlines()

    prompt_data = {
        "framework": "",
        "endpoint": "",
        "fields": []
    }

    for line in lines:
        if line.startswith("framework:"):
            prompt_data["framework"] = line.split(":")[1].strip()
        elif line.startswith("endpoint:"):
            prompt_data["endpoint"] = line.split(":")[1].strip()
        elif "-" in line:
            prompt_data["fields"].append(line.strip().split("-")[1].strip())
    return prompt_data


def parse_code(text, path="tester/", filename="apis.py"):
    match = re.search(r"```python(.*?)```", text, re.DOTALL)
    code = match.group(1).strip() if match else ""
    with open(path+filename, 'w') as f:
        f.write(code)
        f.close()


if __name__ == "__main__":
    with open("prompt", 'r') as f:
        prompt = f.read()
        f.close()

    print(prompt)

    resp = generate_framework(prompt)

    # with open('test.json', 'r') as f:
    #     data = json.load(f)
    #     f.close()
    # text = data['candidates'][0]['content']['parts'][0]['text']

    parse_code(resp)

