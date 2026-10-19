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

with pool.connection() as connection:
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT id, file_path, chunk_number, code
            FROM code_chunks
            ORDER BY id
            """
        )

        rows = cursor.fetchall()
        print(rows)

        for row in rows:
            print(row)

pool.close()