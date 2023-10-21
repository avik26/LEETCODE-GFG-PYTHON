#User function Template for python3

class Solution:
    def longestSubsequence(self, A, N):
        # Initialize a list to store the increasing subsequence.
        lis = [A[0]]
        
        for i in range(1, N):
            if A[i] > lis[-1]:
                # If the current element is greater than the last element in lis, append it.
                lis.append(A[i])
            else:
                # Use binary search to find the position where A[i] should be inserted.
                left, right = 0, len(lis) - 1
                while left < right:
                    mid = (left + right) // 2
                    if lis[mid] < A[i]:
                        left = mid + 1
                    else:
                        right = mid
                # Replace the element at the found position with A[i].
                lis[left] = A[i]
        
        # Return the length of the longest increasing subsequence.
        return len(lis)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        a = [ int(x) for x in input().split() ]
        ob=Solution()
        print(ob.longestSubsequence(a,n))
# } Driver Code Ends