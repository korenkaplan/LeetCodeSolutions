"""
Medium -> Jump Game:
--------------------
You are given an integer array nums. You are initially positioned at the array's first index, and each element
in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.


Example 1:

Input: nums = [2,1,0,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
"""
from decorators import measure_time


@measure_time
def func(nums: list[int]) -> bool:
    # Initialize the required jump distance to 1
    jump_required = 1

    # Initialize a flag to track whether it's possible to reach the end
    can_jump = True

    # Loop through the list in reverse order, starting from the second-to-last element
    for num in nums[-2::-1]:
        # Check if the current number is greater than or equal to the required jump distance
        can_jump = num >= jump_required

        # Update the required jump distance:
        # If the current number is not sufficient for a jump, increment the required jump distance,
        # otherwise reset it to 1 as we can jump from this position
        jump_required = jump_required + 1 if not can_jump else 1

    # Return whether it's possible to reach the end of the list
    return can_jump


nums = [3, 2, 1, 0, 4]
print(func(nums))
nums = [3, 2, 0, 1, 4]
print(func(nums))
