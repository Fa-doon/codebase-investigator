from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI() #create FastAPI app

class Question(BaseModel):
    question: str

@app.post("/ask")
def ask(question: Question): 
    return {"question": question.question}