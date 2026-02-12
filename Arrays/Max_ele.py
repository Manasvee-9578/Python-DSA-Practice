"""
Problem: Find Maximum Element in Array
Concept: Basic Traversal
Time Complexity: O(n)
Space Complexity: O(1)
"""
def find_max(arr):
    if not arr:
        return None # Return None for empty array
    
    maximum = arr[0]
    for num in arr:
        if num > maximum:
            maximum = num
    return maximum  

# Example usage
arr = [3, 1, 4, 1, 5, 9]
max_element = find_max(arr)
print("Maximum element in the array is:", max_element)