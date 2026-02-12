"""
Problem: Find Second Largest Element
Concept: Single Pass Tracking
Time Complexity: O(n)
Space Complexity: O(1)
"""

def second_large(arr):
    n = len(arr)
    if n<2:
        return None  # Not enough elements for second largest
    
    first = second = float('-inf')

    for num in arr:
        if num > first:
            second = first
            first = num
        elif first > num > second and num != first:
            second = num
    return second

# Example usage
arr = [3, 1, 4, 1, 5, 9]
result = second_large(arr)
print("Second Largest Element:", result)
