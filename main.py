import os
from os import path
from enum import Enum


class difficulties(Enum):
    e = 'Easy'
    m = 'Medium'
    h = 'Hard'


def create_file(file_name: str, difficulty: difficulties):
    folder_path = path.abspath(difficulty.value)
    if not path.exists(folder_path):
        os.makedirs(folder_path)
    full_path = os.path.join(folder_path, f'{file_name.lower().replace(" ", "_")}.py')
    with open(full_path, 'w') as file:
        file.write(f'''"""
{difficulty.value} -> {file_name}:
{'-' * (len(file_name) + len(difficulty.value) + 3)}
"""
from decorators import measure_time


@measure_time
def func():
    pass
''')


difficulty = difficulties.e
file_name = 'Roman to Integer'
create_file(file_name, difficulty)
