import ast

with open("sample_codebase/example.py", "r", encoding="utf-8") as source_file:
    content = source_file.read()

tree = ast.parse(content)

for node in ast.walk(tree):
    if isinstance(node, ast.FunctionDef):
        print(node.name)

# print(ast.dump(tree))