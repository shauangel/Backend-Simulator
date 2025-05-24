import os
import json
import random
from faker import Faker

fake = Faker()


def generate_fake(data, n=10, path="result", filename="data.json"):
    f_data = []
    for _ in range(n):
        entry = {}
        for name, typ in data.items():
            entry[name] = fake_value(name, typ)
        f_data.append(entry)

    os.makedirs(path, exist_ok=True)

    with open(os.path.join(path, filename), 'w') as f:
        json.dump(f_data, f)
        f.close()

    return f_data


def fake_value(name, typ):
    if typ == "str":
        return fake.sentence() if "desc" in name else fake.word()
    if typ == "int":
        return random.randint(0, 100)
    if typ == "bool":
        return random.choice([True, False])
    if typ == "date":
        return str(fake.date())
    if typ == "email":
        return fake.email()
    return f"unknown_{typ}"


if __name__ == "__main__":
    test = {"title": "str", "due_date": "date", "is_done": "bool"}
    f = generate_fake(test)
    print(f)
