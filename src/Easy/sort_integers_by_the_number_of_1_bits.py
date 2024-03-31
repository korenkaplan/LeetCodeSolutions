"""
Easy -> Sort Integers by The Number of 1 Bits:
--------------------------------------------
"""
from decorators import measure_time
from collections import Counter

"""
When you return a tuple from the sorting key function, Python compares the elements of the tuples in lexicographical
order. That means it compares the first element of each tuple. If they are equal, it compares the second elements, and so on.
"""


@measure_time
def sortByBits(arr: list[int]):
    # Sort the array first by the amount of '1' bits, if they equal then by number
    return sorted(arr, key=lambda num: (bin(num).count('1'), num))


def sortByBits_2(arr: list[int]):
    # Sort the array first by the amount of '1' bits, if they equal then by number
    return sorted(arr, key=lambda x: (x.bit_count(), x))


arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(sortByBits_2(arr))
