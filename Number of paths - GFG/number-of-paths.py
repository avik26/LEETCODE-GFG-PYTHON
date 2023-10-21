#User function Template for python3

class Solution:
    def numberOfPaths(self, M, N):
        MOD = 10**9 + 7

        # Initialize result as 1
        result = 1

        # Use the multiplicative formula for combinations
        for i in range(1, M):
            result = (result * (N + i - 1)) % MOD
            result = (result * pow(i, MOD - 2, MOD)) % MOD

        return result
#{ 
 # Driver Code Starts
#Initial Template for Python 3

        

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        M, N = map(int, input().split())
        ans = ob.numberOfPaths(M, N)
        print(ans)




# } Driver Code Ends