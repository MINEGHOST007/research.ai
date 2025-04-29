from fastapi import FastAPI
from typing import Union
from tools import process_input


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/query")
def read_query(q: Union[str, None] = None):
    if q:
        result = process_input(q)
        return {"papers": result}
    return {"query": "No query provided"}

