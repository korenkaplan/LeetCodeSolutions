"""
Easy -> Merge Sorted Array:
--------------------------------------
"""

from decorators import measure_time


@measure_time
def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:

    nums1[:] = nums1[:m]  # Truncate nums1 to length m
    nums2 = nums2[:n]     # Truncate nums2 to length n
    nums1.extend(nums2)   # Extend nums1 with nums2
    nums1.sort()          # Sort nums1 in place





nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)