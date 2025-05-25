from fastapi import FastAPI, Request, HTTPException, Body
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict
from models import generate_framework, parse_code, pack_result
from fake_data import generate_fake
import uvicorn

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Open to all — for testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate-api")
def generate_api(payload: Dict = Body(...)):
    # Use payload directly as a dict
    print("Received JSON:", payload)

    # Generate code using Gemini model
    resp = generate_framework(payload)

    # Parse and save generated code
    parse_code(resp)

    return {"status": "success", "message": "API code generated"}


@app.post("/generate-fake-data")
def generate_fake_data(payload: Dict = Body(...)):
    # Call your fake_data module
    f = generate_fake(payload)
    return {"data": f}


@app.get("/download")
def download():
    try:
        pack_result()
    except FileNotFoundError:
        return HTTPException(status_code=404, detail="Result directory not found.")
    return FileResponse(
        path="/tmp/result.zip",
        filename="backend_result.zip",
        media_type="application/zip"
    )


@app.get("/hello")
def hello():
    return "Welcome to Back-end Simulator :D"


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
