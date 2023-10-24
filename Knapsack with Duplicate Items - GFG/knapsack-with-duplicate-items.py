#User function Template for python3

class Solution:
    def knapSack(self, N, W, val, wt):
        # Create a list to store the maximum value that can be obtained for each weight
        dp = [0] * (W + 1)
        
        # Iterate through each item
        for i in range(N):
            # For each weight from 1 to W, calculate the maximum value
            for w in range(1, W + 1):
                # Check if the current item can be included in the knapsack
                if wt[i] <= w:
                    # If included, calculate the maximum value either by including the item
                    # or not including the item
                    dp[w] = max(dp[w], dp[w - wt[i]] + val[i])
        
        # The final element of dp contains the maximum value for the given weight limit
        return dp[W]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, W = [int(x) for x in input().split()]
        val = input().split()
        for itr in range(N):
            val[itr] = int(val[itr])
        wt = input().split()
        for it in range(N):
            wt[it] = int(wt[it])
        
        ob = Solution()
        print(ob.knapSack(N, W, val, wt))
# } Driver Code Ends