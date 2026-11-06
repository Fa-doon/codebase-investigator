from psycopg_pool import ConnectionPool
from dotenv import load_dotenv
import os
import string
import ast

load_dotenv()

connection_sting = (
    f"host={os.getenv('DB_HOST')} "
    f"port={os.getenv('DB_PORT')} "
    f"dbname={os.getenv('DB_NAME')} "
    f"user={os.getenv('DB_USER')} "
    f"password={os.getenv('DB_PASSWORD')}"
)

pool = ConnectionPool(connection_sting)

codebase_directory = os.path.join(os.getcwd(), "sample_codebase")
file_path = os.path.join(codebase_directory, "example.py")

question = "How does the add() function work?"

# 1. Get the user's question
question = "How does the add() function work?"

cleaned_question = question.replace("?", "")
words = cleaned_question.split()

stop_words = ["how", "does", "the", "do", "is", "a", "an"]

search_terms = []

for word in words:
    word = word.strip(string.punctuation)

    if word.lower() not in stop_words:
        search_terms.append(word)

print("Search terms:", search_terms)

# 2. Read the source file and extract function names
with open(file_path, "r", encoding="utf-8") as source_file:
    content = source_file.read()

tree = ast.parse(content)

function_names = []

for node in ast.walk(tree):
    if isinstance(node, ast.FunctionDef):
        function_names.append(node.name)

print("Function names:", function_names)

# 3. Match search terms against function names
matched_functions = []

for term in search_terms:
    if term in function_names:
        matched_functions.append(term)

print("Matched functions:", matched_functions)

code = ""

for function_name in matched_functions:
    search_pattern = f"%def {function_name}(%"

    with pool.connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT chunk_number, code
                FROM code_chunks
                WHERE file_path = %s
                AND code ILIKE %s
                ORDER BY chunk_number
                """,
                (file_path, search_pattern)
            )

            rows = cursor.fetchall()

    for row in rows:
        code += row[1] + "\n"


prompt = f"""
Question: {question}

Code:
{code}
"""

print(prompt)

pool.close()