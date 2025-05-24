from models import generate_framework, parse_code
from fake_data import generate_fake_data

import json
import re

if __name__ == "__main__":
    # Setup prompts
    setup = {
        "framework": "Flask",
        "endpoints": [{"name": "task",
                       "field": {"title": "str", "due_date": "date", "is_done": "bool"},
                       "method": ['get', 'post']}
                      ]
    }

    # Generate framework and API files
    resp = generate_framework(setup)
    parse_code(resp, filename='test_json_input.py')

    # # Make fake data
    # generate_fake_data()

    # Run apis


