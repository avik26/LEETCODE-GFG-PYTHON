class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0:
            return []

        ans = [[1]]

        for i in range(1, numRows):
            new_row = [1]
            for j in range(1, i):
                new_row.append(ans[i - 1][j - 1] + ans[i - 1][j])
            new_row.append(1)
            ans.append(new_row)

        return ans
