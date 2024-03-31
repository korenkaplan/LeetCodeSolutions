"""
Medium -> Remove Duplicates from Sorted Array II:
-------------------------------------------------
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""
from decorators import measure_time
from collections import Counter

# Counter({1: 4, 0: 2, 3: 2, 2: 1})
# @measure_time
# def func(nums: list):
#     repeat_counter = 1
#     insert_index = 1
#     prev = nums[0]
#     for index, value in enumerate(nums[1:]):
#         current_num_to_check = value
#         # if the same number still repeating
#         if current_num_to_check == prev:
#             repeat_counter += 1
#             # if appears for the 3 time or more change the insert index
#             if repeat_counter > 2:
#                 insert_index = index
#         else:
#             nums[]








# nums = [0,0,1,1,1,1,2,3,3]
# func(nums)



