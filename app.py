from fastapi import FastAPI, Request
from typing import Dict
from fastapi import Body
from models import generate_framework, parse_code
from fake_data import generate_fake
import uvicorn

app = FastAPI()


@app.post("/generate-api")
def generate_api(payload: Dict = Body(...)):
    # Use payload directly as a dict
    print("Received JSON:", payload)

    # Generate code using Gemini model
    resp = generate_framework(payload)

    # Parse and save generated code
    parse_code(resp, filename='test_local.py')

    return {"status": "success", "message": "API code generated"}


@app.post("/generate-fake-data")
def generate_fake_data(payload: Dict = Body(...)):
    # Call your fake_data module
    f = generate_fake(payload)
    return {"data": f}


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
