"""
Problem: Linear Search
Concept: Sequential Traversal
Time Complexity: O(n)
Space Complexity: O(1)

Description:
Search for a target element in an array by checking each element one by one.
Returns index if found, otherwise -1.
"""

""" 
When To Use?
Array MUST be sorted
You want fast search
"""
def linear_search(arr, target):
    n = len(arr)
    for i in range(n):
        if arr[i] == target:
            return i  # Target found, return index
    return -1  # Target not found, return -1

# Example usage
arr = [5, 3, 2, 8, 1]
target = 2
result = linear_search(arr, target)
print("Target found at index:", result)  