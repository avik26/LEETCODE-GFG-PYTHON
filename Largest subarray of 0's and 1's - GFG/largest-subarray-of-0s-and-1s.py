#User function Template for python3
class Solution:
    def maxLen(self, arr, N):
        max_length = 0  # Initialize the maximum length to 0
        prefix_sum = 0  # Initialize the running sum to 0
        prefix_sum_dict = {}  # Initialize a dictionary to store prefix sums

        for i in range(N):
            if arr[i] == 1:
                prefix_sum += 1
            else:
                prefix_sum -= 1

            # If the running sum is 0, update the maximum length
            if prefix_sum == 0:
                max_length = i + 1

            # If the running sum is not zero, check if it has been seen before
            if prefix_sum in prefix_sum_dict:
                max_length = max(max_length, i - prefix_sum_dict[prefix_sum])
            else:
                prefix_sum_dict[prefix_sum] = i

        return max_length


#{ 
 # Driver Code Starts
#Initial Template for Python 3


t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().maxLen(a, len(a))
    print(s)
# } Driver Code Ends