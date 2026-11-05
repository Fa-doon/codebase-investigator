from psycopg_pool import ConnectionPool
from dotenv import load_dotenv
import os
import string

load_dotenv()

connection_sting = (
    f"host={os.getenv('DB_HOST')} "
    f"port={os.getenv('DB_PORT')} "
    f"dbname={os.getenv('DB_NAME')} "
    f"user={os.getenv('DB_USER')} "
    f"password={os.getenv('DB_PASSWORD')}"
)

pool = ConnectionPool(connection_sting)

# search_term = "%example.py%"
codebase_directory = os.path.join(os.getcwd(), "sample_codebase")

def get_file_code(file_path):
    full_code = ""
    file_path = os.path.join(os.getcwd(), "sample_codebase", file_path)
   

    with pool.connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                 SELECT chunk_number, code
                 FROM code_chunks
                 WHERE file_path = %s
                 AND code ILIKE %s
                """,
                (file_path, "%greet%")
            )

            rows = cursor.fetchall()


        for row in rows:
            # full_code += row[3] + "\n"
            full_code += row[1] + "\n"
                
        return full_code

code = get_file_code("example.py")
# if (code):
#  print(code)

question = "How does the add() function work?"

cleaned_question = question.replace("?", "")
words = cleaned_question.split()
stop_words = ["how", "does", "the", "do", "is", "a", "an"]

search_terms = []

for word in words:
    word = word.strip(string.punctuation)

    if word.lower() not in stop_words:
        search_terms.append(word)

print(search_terms)

print(words)

prompt = f"""
Question: {question}

Code:
{code}
"""

print(prompt)

pool.close()