#User function Template for python3
class Solution:
    def maxSumIS(self, Arr, n):
        if n == 1:
            return Arr[0]

        # Initialize an array to store the maximum sum of strictly increasing subsequences
        maxSum = [0] * n

        # Initialize maxSum with the values of the input array
        for i in range(n):
            maxSum[i] = Arr[i]

        # Dynamic programming to find the maximum sum
        for i in range(1, n):
            for j in range(i):
                if Arr[i] > Arr[j]:
                    maxSum[i] = max(maxSum[i], maxSum[j] + Arr[i])

        # Find the maximum value in the maxSum array
        result = max(maxSum)
        
        return result
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.maxSumIS(Arr,n)
		print(ans)

# } Driver Code Ends