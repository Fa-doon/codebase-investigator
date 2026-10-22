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

codebase_directory = os.path.join(os.getcwd(), "sample_codebase")
chunk_size = 3

for root, directories, files in os.walk(codebase_directory):
    for file in files:
        file_path = os.path.join(root, file)

        with open(file_path, "r", encoding="utf-8") as source_file:
            content = source_file.read()

        lines = content.splitlines()

        with pool.connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    DELETE FROM code_chunks
                    WHERE file_path = %s
                    """,
                    (file_path,)
                )

                for start in range(0, len(lines), chunk_size):
                    chunk = lines[start:start + chunk_size]
                    code = "\n".join(chunk)

                    chunk_number = start // chunk_size + 1

                    cursor.execute(
                        """
                        INSERT INTO code_chunks
                            (file_path, chunk_number, code)
                        VALUES (%s, %s, %s)
                        """,
                        (file_path, chunk_number, code)
                    )

pool.close()