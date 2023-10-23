#User function Template for python3
class Solution:
    def immediateSmaller(self, arr, n):
        # Iterate through the array in reverse order
        for i in range(n - 1):
            # Check if the next adjacent element is smaller
            if arr[i] > arr[i + 1]:
                arr[i] = arr[i + 1]
            else:
                arr[i] = -1
        # The last element always has no element to the right, so set it to -1
        arr[n - 1] = -1
#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        n=int(input())
        arr=[int(x) for x in input().split()]
        ob = Solution()
        ob.immediateSmaller(arr,n)
        for x in arr:
            print(x, end=" ")
        print()
# } Driver Code Ends