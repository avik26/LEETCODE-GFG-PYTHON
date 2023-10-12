class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        # Initialize the dp array to store the number of ways to reach each step
        dp = [0] * (n + 1)
        dp[1] = 1  # There is only one way to reach the first step
        dp[2] = 2  # There are two ways to reach the second step
        
        # Calculate the number of ways for the remaining steps
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]
