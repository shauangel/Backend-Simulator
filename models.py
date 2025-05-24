from google import genai
from google.genai.types import HttpOptions
import re
import os

api_key = os.environ.get("GENAI_API_KEY")
if not api_key:
    raise RuntimeError("Missing Gemini API key!")


# with open("keys", "r") as f:
#     api_key = f.readline()
#     f.close()


def generate_framework(setup):
    prompt = "Create a " + setup['framework'] + "RESTAPI with the following specification: \n\nEndpoints \n"
    for e in setup['endpoints']:
        prompt += ("- /{e['name']}: \n" +
                   "  - Methods: " + ", ".join(e['method']) + "\n" +
                   "  - Fields: \n")
        for k, v in e['field'].items():
            prompt += "    - " + k + ": " + v + "\n"
    prompt += "\nAdd Swagger. Use flask_swagger_ui for Swagger with flask. Use sqlalchemy for database."

    print(prompt)

    client = genai.Client(http_options=HttpOptions(api_version="v1"), api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=prompt,
    )
    print(response.text)
    return response.text


def parse_code(text, path="tester", filename="apis.py"):
    match = re.search(r"```python(.*?)```", text, re.DOTALL)
    code = match.group(1).strip() if match else ""

    # Ensure the directory exists
    os.makedirs(path, exist_ok=True)

    with open(os.path.join(path, filename), 'w') as f:
        f.write(code)
        f.close()


# if __name__ == "__main__":
    # with open("prompt", 'r') as f:
    #     prompt = f.read()
    #     f.close()
    #
    # print(prompt)
    #
    # resp = generate_framework(prompt)

    # with open('test.json', 'r') as f:
    #     data = json.load(f)
    #     f.close()
    # text = data['candidates'][0]['content']['parts'][0]['text']

    # parse_code(resp)

