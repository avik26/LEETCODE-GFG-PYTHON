class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []  # Stack to store the indices of open parentheses
        max_length = 0  # Maximum length of valid parentheses 

        # Initialize a variable to keep track of the last invalid index
        last_invalid = -1

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                if not stack:
                    # If the stack is empty, the current ')' is invalid
                    last_invalid = i
                else:
                    # Pop the last open parenthesis
                    stack.pop()
                    if not stack:
                        # If the stack is empty, the substring from last_invalid to i is valid
                        max_length = max(max_length, i - last_invalid)
                    else:
                        # If the stack is not empty, the substring from the last element in the stack to i is valid
                        max_length = max(max_length, i - stack[-1])

        return max_length
