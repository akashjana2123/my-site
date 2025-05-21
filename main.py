from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from typing import List, Optional
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

with open("q-vercel-python.json", "r") as f:
    data = json.load(f)

marks_dict = {entry["name"]: entry["marks"] for entry in data}

@app.get("/api")
def get_marks(name: Optional[List[str]] = Query(None)):
    if not name:
        # No name param: return all marks
        return JSONResponse(content={"marks": data})
    else:
        # Return marks for requested names in order
        result = [marks_dict.get(n, None) for n in name]
        return JSONResponse(content={"marks": result})
