"""
Medium -> Zigzag Conversion:
----------------------------
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
 (you may want to display this pattern in a fixed font for better legibility)
P---A---H---N
A-P-L-S-I-I-G
Y---I---R
And then read line by line: "PAHN APLSIIG YIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);
Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P-----I----N-
A---L-S--I--G
Y-A---H-R----
P-----I------
Example 3:

Input: s = "A", numRows = 1
Output: "A"
"""
from decorators import measure_time

@measure_time
def convert(s: str, numRows: int) -> str:
    # If numRows is 1 or greater than or equal to the length of s,
    # return the input string as it is.
    if numRows == 1 or numRows >= len(s):
        return s

    # Create a list to hold each row of the zigzag pattern.
    result = [''] * numRows

    # Initialize index to keep track of the current row,
    # and step to control the direction of movement in the zigzag pattern.
    index, step = 0, 1

    # Iterate through each character in the input string.
    for char in s:
        # Append the current character to the row indicated by index.
        result[index] += char

        # Update the step based on the current row.
        if index == 0:
            # If index is 0, change the direction to downward.
            step = 1
        elif index == numRows - 1:
            # If index reaches the last row, change the direction to upward.
            step = -1

        # Move to the next row according to the direction specified by step.
        index += step

    # Concatenate all rows to form the final zigzag pattern.
    return ''.join(result)


# Test cases
print(convert("PAYPALISHIRING", 3))  # Output: "PAHNAPLSIIGYIR"
print(convert("PAYPALISHIRING", 4))  # Output: "PINALSIGYAHRPI"
print(convert("A", 1))  # Output: "A"

