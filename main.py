from fastapi import FastAPI
from search import search_businesses

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Business Research Agent is running"}

@app.get("/search")
def search(query: str):
    return search_businesses(query)