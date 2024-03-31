"""
a module for creating the exercise file and the test file
"""
import os
from enum import Enum
from os import path, makedirs


# region Constants
class difficulties(Enum):
    e = 'Easy'
    m = 'Medium'
    h = 'Hard'


TEST_FOLDER_URL = path.abspath('tests')
EXERCISE_FOLDER_URL = path.abspath('src')
TEST_PREFIX = 'test_'


# endregion

def to_file_name(string: str):
    return string.replace(" ", "_").lower()


#  a function to create the text for the exercise file
def create_exercise_text(file_name, difficulty):
    return f'''"""
{difficulty.value} -> {file_name}:
{'-' * (len(file_name) + len(difficulty.value) + 5)}
"""
from LeetCode.decorators import measure_time


@measure_time
def func():
    pass


print(func())
'''


#  a function to create the text for the test file
def create_test_text(filename, difficulty: difficulties):
    return f'''
import pytest
from LeetCode.src.{difficulty.value}.{filename} import func


@pytest.mark.parametrize(", expected", [])
def test_{filename}(, expected):
    result = func()
    assert result == expected
'''


# a function to create the exercise file
def create_file_exercise(file_name: str, text: str, folder_path: str):
    if not path.exists(folder_path):
        makedirs(folder_path)
    full_path = path.join(folder_path, f'{file_name}.py'.lower().replace(" ", "_"))
    with open(full_path, 'w') as file:
        file.write(text)


# a function to create the test file
def create_test_file(file_name: str, difficulty: difficulties):
    text = create_test_text(file_name)
    prefix = "test_"
    # create_file(file_name, text, folder_path)
    folder_path = path.abspath(f'{prefix}{difficulty.value}')
    full_p = path.join(folder_path, f'{prefix}{file_name.replace(" ", "_")}.py')
    print(full_p)
    with open(full_p, 'w') as file:
        file.write(text)


# the function to create EVERYTHING
def create_file(file_name: str, text: str, folder_path: str, difficulty: difficulties, prefix=''):
    folder_with_difficulty_path = path.join(folder_path, difficulty.value)
    if not path.exists(folder_with_difficulty_path):
        makedirs(folder_with_difficulty_path)
    full_path = path.join(folder_with_difficulty_path, f'{prefix}{file_name}.py')
    with open(full_path, 'w') as file:
        file.write(text)


def create_exercise_and_test_file(file_name: str, difficulty: difficulties):
    file_name = to_file_name(file_name)
    # Create the text for the files
    test_text = create_test_text(file_name, difficulty)
    exercise_text = create_exercise_text(file_name, difficulty)

    # Create the test file
    create_file(file_name, test_text, TEST_FOLDER_URL, difficulty, prefix=TEST_PREFIX)
    create_file(file_name, exercise_text, EXERCISE_FOLDER_URL, difficulty)
