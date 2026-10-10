
import os

current_directory = os.getcwd()

items = os.listdir(current_directory)

for item in items:
    item_path = os.path.join(current_directory, item)

    if os.path.isfile(item_path):
        print(f"File: {item}")
    elif os.path.isdir(item_path):
        print(f"Directory: {item}")
