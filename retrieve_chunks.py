from psycopg_pool import ConnectionPool
from dotenv import load_dotenv
import os

load_dotenv()

connection_sting = (
    f"host={os.getenv('DB_HOST')} "
    f"port={os.getenv('DB_PORT')} "
    f"dbname={os.getenv('DB_NAME')} "
    f"user={os.getenv('DB_USER')} "
    f"password={os.getenv('DB_PASSWORD')}"
)

pool = ConnectionPool(connection_sting)

search_term = "%example.py%"

with pool.connection() as connection:
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT id, file_path, chunk_number, code
            FROM code_chunks
            WHERE file_path LIKE %s
            ORDER BY chunk_number
            """,
            (search_term,)
        )

        rows = cursor.fetchall()

        full_code = ""

        for row in rows:
            full_code += row[3] + "\n"
            
        print(full_code)

pool.close()