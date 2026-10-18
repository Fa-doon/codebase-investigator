import os

codebase_directory = os.path.join(os.getcwd(), "sample_codebase")
chunk_size = 3

for root, directories, files in os.walk(codebase_directory):
    for file in files:
        file_path = os.path.join(root, file)

        with open(file_path, "r", encoding="utf-8") as source_file:
            content = source_file.read()

        lines = content.splitlines()

        for start in range(0, len(lines), chunk_size):
            chunk = lines[start:start + chunk_size]
            code = "\n".join(chunk)

            print(f"\nFile: {file_path}")
            print(f"Chunk number: {start // chunk_size + 1}")
            print(code)