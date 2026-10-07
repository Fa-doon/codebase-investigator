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

# print(connection)

print(os.getenv("DB_HOST"))

# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS test (
#         id SERIAL PRIMARY KEY,
#         name TEXT    
#     )
# """)

# connection.commit()


app = FastAPI() #create FastAPI app

class Question(BaseModel):
    question: str

class TestData(BaseModel):
    name: str

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

