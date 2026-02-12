"""
Problem: Check If Array Is Sorted
Concept: Adjacent Comparison
Time Complexity: O(n)
Space Complexity: O(1)
"""

def is_sorted(arr):
    n = len(arr)

    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            return "Array is not sorted!!"
    return "Array is sorted!!" 

# Example usage
arr = [1, 2, 3, 4, 5]
print(is_sorted(arr)) 
arr = [5, 4, 3, 2, 1]
print(is_sorted(arr))