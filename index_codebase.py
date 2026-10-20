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

# find files in sample_codebase
for root, directories, files in os.walk(codebase_directory):
    for file in files:
        file_path = os.path.join(root, file) # get full path

        with open(file_path, "r", encoding="utf-8") as source_file: # read content
            content = source_file.read()

        lines = content.splitlines() # split content into chunks

        for start in range(0, len(lines), chunk_size):
            chunk = lines[start:start + chunk_size]
            code = "\n".join(chunk)

            chunk_number = start // chunk_size + 1

            with pool.connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(                      #save chunk
                        """
                        INSERT INTO code_chunks (file_path, chunk_number, code)
                        VALUES (%s, %s, %s)
                        ON CONFLICT (file_path, chunk_number) DO NOTHING
                        """,
                        (file_path, chunk_number, code)
                    )

pool.close()