from models import generate_framework, parse_code, parse_prompt
from fake_data import generate_fake_data

import json
import re

if __name__ == "__main__":
    # Setup prompts
    prompt = parse_prompt()
    print(prompt)

    # Generate framework and API files
    resp = generate_framework(prompt)
    parse_code(resp, filename='apis_swagger.py')

    # Make fake data
    generate_fake_data()

    # Run apis


