"""
Medium -> Rotate Array:
-----------------------
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
"""
from decorators import measure_time
from collections import deque


@measure_time
def func(nums, k):
    nums_deque = deque(nums)
    for _ in range(k):
        new_head = nums_deque.pop()
        nums_deque.appendleft(new_head)
    nums[:] = list(nums_deque)



nums, k = [1, 2, 3, 4, 5, 6, 7], 3
func(nums, k)
print(nums)
