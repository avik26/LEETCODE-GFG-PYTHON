class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        col1, row1, col2, row2 = s[0], int(s[1]), s[3], int(s[4])
        return [f"{chr(col)}{row}" for col in range(ord(col1), ord(col2) + 1) for row in range(row1, row2 + 1)]
