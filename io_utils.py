import os

current_file_path = os.path.abspath(__file__)

project_root = os.path.dirname(current_file_path)


def name_to_path(file_name: str) -> str:
    return os.path.join(project_root, 'data', file_name)


def read_file_to_list(file_name):
    file_path = name_to_path(file_name)
    print(file_path)
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]
