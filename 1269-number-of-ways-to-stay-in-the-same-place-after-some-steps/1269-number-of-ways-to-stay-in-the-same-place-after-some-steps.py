class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7
        maxPosition = min(steps, arrLen - 1)  # The maximum position you can reach is either steps or arrLen - 1.

        # Initialize a 2D array to keep track of the number of ways to reach each position.
        dp = [[0] * (maxPosition + 1) for _ in range(steps + 1)]
        dp[0][0] = 1  # There is one way to start at position 0 with 0 steps.

        for i in range(1, steps + 1):
            for j in range(maxPosition + 1):
                dp[i][j] = dp[i - 1][j]  # Stay in the same position.

                if j > 0:
                    dp[i][j] += dp[i - 1][j - 1]  # Move one step to the left.

                if j < maxPosition:
                    dp[i][j] += dp[i - 1][j + 1]  # Move one step to the right.

                dp[i][j] %= MOD

        return dp[steps][0]  # Return the number of ways to reach position 0 after 'steps' steps.
