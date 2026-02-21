"""
Problem: Maximum Subarray
Pattern: Kadane’s Algorithm
Time Complexity: O(n)
Space Complexity: O(1)

Description:
Given an integer array nums,
find the contiguous subarray with the largest sum.

Approach:
At each position, decide whether to start fresh
or extend previous subarray.
Track maximum seen so far.
"""

class Solution(object):
    def maxSubArray(self, nums):
        max_sum = nums[0]
        current_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)

        return max_sum
    