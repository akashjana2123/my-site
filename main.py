from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load the JSON data once
with open("q-vercel-python.json", "r") as f:
    data = json.load(f)

@app.get("/api")
def get_marks(name: list[str] = []):
    name_to_marks = {entry["name"]: entry["marks"] for entry in data}
    marks = [name_to_marks.get(n, None) for n in name]
    return {"marks": marks}
