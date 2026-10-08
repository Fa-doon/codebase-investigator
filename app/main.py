from fastapi import FastAPI
from pydantic import BaseModel
import os
from psycopg_pool import ConnectionPool

from dotenv import load_dotenv

load_dotenv()

pool = ConnectionPool(
    conninfo=(
        f"host={os.getenv('DB_HOST')} "
        f"port={os.getenv('DB_PORT')} "
        f"dbname={os.getenv('DB_NAME')} "
        f"user={os.getenv('DB_USER')} "
        f"password={os.getenv('DB_PASSWORD')}"
    )
)

#create FastAPI app
app = FastAPI() 

# Pydantic models
class Question(BaseModel):
    question: str

class TestData(BaseModel):
    name: str

class CodeChunk(BaseModel):
    file_path: str
    chunk_number: int
    code: str



@app.post("/ask")
def ask(question: Question): 
    return {"question": question.question}


@app.post("/test")
def create_test(data: TestData):
    with pool.connection() as connection:
       with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO test (name)
                VALUES (%s)

            """, (data.name,))

    return { "message": "Created"}

@app.get("/test")
def get_test():
    with pool.connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM test")
            rows = cursor.fetchall()

    return {"rows": rows}

@app.post("/code-chunks")
def create_code_chunk(chunk: CodeChunk):
    with pool.connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO code_chunks (file_path, chunk_number, code)
                VALUES (%s, %s, %s)
            """, (
                chunk.file_path,
                chunk.chunk_number,
                chunk.code
            ))

    return {"message": "Code chunk created"}

