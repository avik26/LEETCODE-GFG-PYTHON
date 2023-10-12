class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Function to find the longest increasing subsequence (LIS) for an array
        def LIS(arr):
            n = len(arr)
            dp = [1] * n
            for i in range(n):
                for j in range(i):
                    if arr[i] > arr[j]:
                        dp[i] = max(dp[i], dp[j] + 1)
            return dp
        
        left_lis = LIS(nums)
        right_lis = LIS(nums[::-1])[::-1]
        
        max_mountain = 0
        for i in range(n):
            if left_lis[i] > 1 and right_lis[i] > 1:
                max_mountain = max(max_mountain, left_lis[i] + right_lis[i] - 1)
        
        return n - max_mountain if max_mountain > 0 else -1
