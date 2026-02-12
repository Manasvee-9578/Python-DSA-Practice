"""
Problem: Reverse an Array
Concept: Two Pointers
Time Complexity: O(n)
Space Complexity: O(1)
"""

def rev_array(arr):
    n = len(arr)
    left = 0
    right = n-1

    while left < right:
        arr[left],arr[right] = arr[right],arr[left]
        left += 1
        right -= 1
    return arr

# Example usage:
print(rev_array([1, 2, 3, 4, 5])) 
print(rev_array(['a', 'b', 'c', 'd']))
print(rev_array([True, False, True]))