import ast

with open("sample_codebase/example.py", "r", encoding="utf-8") as source_file:
    content = source_file.read()

tree = ast.parse(content)

search_terms = ["add", "function", "work"]
function_names = []

for node in ast.walk(tree):
    if isinstance(node, ast.FunctionDef):
        function_names.append(node.name)

print(function_names)

matched_functions = []

for term in search_terms:
    if term in function_names:
        matched_functions.append(term)

print(matched_functions)

     


# print(ast.dump(tree))