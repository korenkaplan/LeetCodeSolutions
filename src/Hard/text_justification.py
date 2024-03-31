"""
Hard -> Text Justification:
---------------------------
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.
"""
from decorators import measure_time

"""
step 1: Start looping through the list and sum length word by word until it reaches max width (or less, not passed max width )
        include one space for each word as it should be calculated in the string length.
step 2: Each time you reach a word and can't add the next word: check how much space you need to fill and divide it by the 
        amount of words in the line -1, and distribute the spaces equally as possible with the remider is in the left side
step 3: Repeat until you reach the end of the words list and if you have only one word it should be left-justified.
step 4: Add each string to a list of words to return.        
"""


@measure_time
def func(words: list[str], maxWidth: int) -> list[str]:
    result = []
    row = []
    row_width = 0
    for index_of_word, word in enumerate(words):
        word_width = len(word)
        if row_width + word_width + len(row) <= maxWidth:
            row.append(word)
            row_width += word_width
        else:
            # Distribute spaces evenly between words in the row
            total_spaces = maxWidth - row_width
            spaces_count = len(row) - 1 if len(row) > 1 else 1
            space_to_add_for_each_word = total_spaces // spaces_count
            extra_spaces = total_spaces % spaces_count

            final_str = ''
            for i, w in enumerate(row):
                final_str += w
                if i < len(row) - 1:
                    final_str += ' ' * space_to_add_for_each_word
                    if extra_spaces > 0:
                        final_str += ' '
                        extra_spaces -= 1

            # If there's only one word in the row, left-justify it
            if len(row) == 1:
                final_str = final_str.ljust(maxWidth)

            result.append(final_str)

            # Reset the row and row_width for the next line
            row = [word]
            row_width = word_width

        # Append the last line if it's the last word
        if index_of_word == len(words) - 1:
            last_line = ' '.join(row)
            last_line = last_line.ljust(maxWidth)
            result.append(last_line)

    return result



words, maxWidth = ["This", "is", "an", "example", "of", "text", "justification."], 16
for word in func(words, maxWidth):
    print(f'"{word}"')
