"""
Problem: Binary Search
Concept: Divide and Conquer
Time Complexity: O(log n)
Space Complexity: O(1)

Description:
Search for a target element in a sorted array.
Returns index if found, otherwise -1.
"""

def binary_search(arr, target):
    n = len(arr)
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1
    return -1

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
result = binary_search(arr, target)
print("Element found at index:", result)  