class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for char in columnTitle:
            # Convert the character to its corresponding value, where 'A' is 1.
            value = ord(char) - ord('A') + 1
            result = result * 26 + value
        return result
