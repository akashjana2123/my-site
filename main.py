from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from typing import List, Optional
import json
import os

app = FastAPI()

# ✅ Enable CORS: allows all origins, headers, and only GET methods
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# ✅ Load JSON data from file at runtime
with open("q-vercel-python.json", "r") as f:
    data = json.load(f)

# ✅ Convert data to dictionary for fast lookup
marks_dict = {entry["name"]: entry["marks"] for entry in data}

# ✅ Root endpoint returns all data — for health check or manual browsing
@app.get("/")
def read_root():
    return JSONResponse(content=data)

# ✅ API endpoint
@app.get("/api")
def get_marks(name: Optional[List[str]] = Query(None)):
    if name is None:
        # No names provided — return empty marks list (IM portals expect valid shape)
        return JSONResponse(content={"marks": []})
    
    # Return list of marks in the same order as query
    result = [marks_dict.get(n, 0) for n in name]  # use 0 if name not found
    return JSONResponse(content={"marks": result})
