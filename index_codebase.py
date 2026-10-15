import os

codebase_directory = os.path.join(os.getcwd(), "sample_codebase")

for root, directories, files in os.walk(codebase_directory):
    for file in files:
        file_path = os.path.join(root, file)
        print(file_path)

        with open(file_path, "r", encoding="utf-8") as source_file:
           content = source_file.read()

        print(content)