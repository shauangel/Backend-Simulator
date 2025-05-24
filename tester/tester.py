import requests

url = "https://backend-simulator-321936462778.us-central1.run.app/generate-fake-data"

data = {"test": "str", "num":"int"}
resp = requests.post(url=url, json=data)
print(resp.content)