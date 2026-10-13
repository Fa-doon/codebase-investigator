from psycopg_pool import ConnectionPool
from dotenv import load_dotenv
import os

load_dotenv()

connection_string = (
    f"host={os.getenv('DB_HOST')} "
    f"port={os.getenv('DB_PORT')} "
    f"dbname={os.getenv('DB_NAME')} "
    f"user={os.getenv('DB_USER')} "
    f"password={os.getenv('DB_PASSWORD')}"
)

pool = ConnectionPool(connection_string)

file_path = "sample_code.py"
chunk_number = 1
code = "def greet(name):\n    return f'Hello, {name}!'"

with pool.connection() as connection:
    with connection.cursor() as cursor:
        cursor.execute(
            """
            INSERT INTO code_chunks (file_path, chunk_number, code)
            VALUES (%s, %s, %s)
            """,
            (file_path, chunk_number, code)
        )

pool.close()
