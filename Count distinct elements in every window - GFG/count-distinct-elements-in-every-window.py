class Solution:
    def countDistinct(self, A, N, K):
        result = []  # Initialize an empty list to store the results
        window = {}  # Initialize an empty dictionary for the current window
        distinct_count = 0  # Initialize a count for distinct elements

        for i in range(N):
            # Add the element at the end of the window to the dictionary
            if A[i] in window:
                window[A[i]] += 1
            else:
                window[A[i]] = 1

            # If the window size exceeds K, remove the element from the beginning
            if i >= K:
                if window[A[i - K]] == 1:
                    del window[A[i - K]]
                else:
                    window[A[i - K]] -= 1

            # If the window size equals K, update the count of distinct elements in the result
            if i >= K - 1:
                result.append(len(window))

        return result

#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        res = Solution().countDistinct(arr, n, k)
        for i in res:
            print (i, end = " ")
        print ()
# } Driver Code Ends