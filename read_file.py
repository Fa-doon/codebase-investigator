
# import os

# current_directory = os.getcwd()

# allowed_extensions = [".py", ".js", ".ts"]

# for root, directories, files in os.walk(current_directory):
#     directories[:] = [
#         directory for directory in directories
#         if directory not in [".venv", ".git", "__pycache__"]
#     ]

#     for file in files:
#         if os.path.splitext(file)[1] in allowed_extensions:
#             file_path = os.path.join(root, file)

#             with open(file_path, "r", encoding="utf-8") as source_file:
#                 content = source_file.read()

#             print(f"\nFile: {file_path}")
#             print(content)


content = """def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b"""

lines = content.splitlines()
print(lines)

chunk_size = 3

for start in range(0, len(lines), chunk_size):
    chunk = lines[start:start + chunk_size]
    print(f"\nChunk starting at line {start + 1}:")
    print("\n".join(chunk))

