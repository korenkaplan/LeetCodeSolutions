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