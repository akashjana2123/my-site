from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import json
from typing import List

app = FastAPI()

# Enable CORS for all origins for GET requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load the marks data once at startup
with open("q-vercel-python.json", "r") as f:
    data = json.load(f)

# Create a dict for quick lookup by name
marks_dict = {entry["name"]: entry["marks"] for entry in data}

@app.get("/api")
def get_marks(name: List[str] = Query(...)):
    # Find marks for each name in the query param, default to None or 0
    result = [marks_dict.get(n, None) for n in name]
    return JSONResponse(content={"marks": result})
