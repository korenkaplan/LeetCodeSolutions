"""
Medium -> Jump Game II:
-----------------------
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].


Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3]
Output: 2
"""
from decorators import measure_time


@measure_time
def min_jumps(nums):
    n = len(nums)
    if n <= 1:
        return 0  # No jumps needed for arrays of length 0 or 1

    jumps = 0  # Initialize the number of jumps
    current_max_reach = 0  # Initialize the maximum reachable index from the current position
    next_max_reach = 0  # Initialize the maximum reachable index from the next position

    for i in range(n - 1):
        next_max_reach = max(next_max_reach, i + nums[i])  # Update the maximum reachable index from the next position

        if i == current_max_reach:  # If the current position is reached, update the current position
            jumps += 1
            current_max_reach = next_max_reach

    return jumps

# Example usage:
nums1 = [2, 3, 1, 1, 4]
print("Minimum number of jumps for nums1:", min_jumps(nums1))  # Output: 2

nums2 = [2, 3]
print("Minimum number of jumps for nums2:", min_jumps(nums2))  # Output: 1

