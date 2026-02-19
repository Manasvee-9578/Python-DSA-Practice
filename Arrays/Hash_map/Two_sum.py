"""
Problem: Two Sum
Pattern: Hashing
Time Complexity: O(n)
Space Complexity: O(n)

Description:
Given an array of integers and a target value,
return indices of the two numbers such that they add up to the target.

Approach:
Use a hash map to store previously seen numbers.
For each element, check if (target - current) exists in the map.
"""
def two_sum(nums,target):
    x = {}
    for i,num in enumerate(nums):
        if target - num in x:
            return [x[target - num],i]
        x[num] = i
# Example usage:
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))