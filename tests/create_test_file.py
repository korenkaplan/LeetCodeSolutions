from os import path
from LeetCode.main import difficulties


def create_test_text(filename):
    return f'''
import pytest
from LeetCode.src.Easy.{filename} import func


@pytest.mark.parametrize(", expected", [])
def test_{filename}(, expected):
    result = func()
    assert result == expected
'''


# region main code
def create_test_file(file_name: str, difficulty: difficulties):
    text = create_test_text(file_name)
    prefix = "test_"
    # create_file(file_name, text, folder_path)
    folder_path = path.abspath(f'{prefix}{difficulty.value}')
    full_p = path.join(folder_path, f'{prefix}{file_name.replace(" ", "_")}.py')
    print(full_p)
    with open(full_p, 'w') as file:
        file.write(text)
    # endregion



file_name = 'Valid Palindrome'
difficulty = difficulties.m
create_test_file(file_name,difficulty)
