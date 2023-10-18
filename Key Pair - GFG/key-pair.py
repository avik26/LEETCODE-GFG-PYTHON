#User function Template for python3
class Solution:
    def hasArrayTwoCandidates(self, arr, n, x):
        seen = set()  # Create a set to store elements encountered so far.

        for num in arr:
            if x - num in seen:
                return True
            seen.add(num)

        return False



#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.hasArrayTwoCandidates(arr, n, x)
        if ans:
            print("Yes")
        else:
            print("No")
        tc -= 1

# } Driver Code Ends