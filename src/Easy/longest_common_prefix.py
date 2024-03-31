"""
Easy -> Longest Common Prefix:
----------------------------
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix amongst the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""
from decorators import measure_time


@measure_time
def longestCommonPrefix(strs: list[str]) -> str:
    """
    Finds the longest common prefix string amongst an array of strings.

    Args:
        strs (List[str]): A list of strings.

    Returns:
        str: The longest common prefix string. If there's no common prefix, returns an empty string ("").

    Example:
        >>> longestCommonPrefix(["flower", "flow", "flight"])
        'fl'
    """
    # Check if the list is empty
    if not strs:
        return ""

    # Sort the list of strings lexicographically
    strs.sort()

    # Initialize an empty list to store the common prefix characters
    res = []

    # Get the first and last words after sorting
    base_prefix_word, last_word_after_sort = strs[0], strs[-1]

    # Determine the minimum length of the prefix based on the lengths of the first and last words
    n = min(len(base_prefix_word), len(last_word_after_sort))

    # Iterate through the characters of the first word (which will be the base prefix word)
    for i in range(n):
        # Compare the corresponding characters of the base prefix word and the last word after sorting
        if base_prefix_word[i] == last_word_after_sort[i]:
            # If the characters match, append the character to the result list
            res.append(base_prefix_word[i])
        else:
            # If there's a mismatch, break the loop
            break

    # Join the characters in the result list to form the longest common prefix string
    return ''.join(res)


strs = ["flower", "flowz", "flowsz", "fz"]
print(longestCommonPrefix(strs))


