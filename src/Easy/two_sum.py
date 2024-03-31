"""
Easy -> Two Sum:
--------------
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""



def two_sum(nums: list[int], target: int) -> list[int]:
    num_indices = {}
    # iterate through the list
    for i, num in enumerate(nums):
        # Calculate the complement needed to reach the target
        complement = target - num
        # If the complement is in the hashmap, return its index along with the current index
        if complement in num_indices:
            return [num_indices[complement], i]
        # Otherwise, store the current number's index in the hashmap
        num_indices[num] = i


nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))
