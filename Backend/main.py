import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from pricing import putOption, callOption


app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

operations_map = {
    "calloption": callOption,
    "putoption": putOption
}

class operationRequest(BaseModel):
    S: float
    K: float
    r: float 
    t: float
    q: float
    vol: float
    operation: str

@app.post("/calculate")
def calculate(request: operationRequest):
    func = operations_map.get(request.operation.lower())
    if not func:
        return {"error" : "Invalid operation. Use 'calloption' or 'putoption'."}
    
    result = func(request.S, request.K, request.r, request.t, request.q, request.vol)
    return {"calculation": result}



