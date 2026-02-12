"""
Problem: Find Minimum Element in Array
Concept: Basic Traversal
Time Complexity: O(n)
Space Complexity: O(1)
"""

def find_min(arr):
    if not arr:
        return None
    
    min_element = arr[0]
    for num in arr:
        if num < min_element:
            min_element = num
    return min_element

# Example usage
arr = [3, 1, 4, 1, 5, 9]
min_element = find_min(arr)
print("The minimum element in the array is: ",min_element)