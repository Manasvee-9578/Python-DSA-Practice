"""
Problem: Valid Parentheses
Pattern: Stack
Time Complexity: O(n)
Space Complexity: O(n)

Description:
Given a string containing just '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

Approach:
Use a stack to track opening brackets.
Match each closing bracket with the top of stack.
"""
class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:
                top = stack.pop() if stack else '#'
                if mapping[char] != top:
                    return False
            else:
                stack.append(char)

        return not stack

solution = Solution()   
print(solution.isValid("()"))       #
print(solution.isValid("()[]{}"))   