class Solution:
    def isPossible(self, N, arr):
        # Calculate the total sum of digits.
        total_sum = sum(arr)

        # If the total sum is divisible by 3, it's possible.
        if total_sum % 3 == 0:
            return 1

        # If the total sum is not divisible by 3, we need to remove the minimum number of digits to make it divisible by 3.
        # Sort the array in ascending order to remove the smallest digits first.
        arr.sort()

        # Find the indices of digits to be removed.
        remove_indices = [-1, -1]

        for i, num in enumerate(arr):
            if num % 3 == total_sum % 3:
                remove_indices[0] = i
                break

        if remove_indices[0] == -1:
            for i, num in enumerate(arr):
                if num % 3 == 3 - total_sum % 3:
                    remove_indices[1] = i
                    break

        # Check if we can remove the minimum number of digits to make it divisible by 3.
        if remove_indices[0] != -1 and remove_indices[1] != -1:
            arr.pop(remove_indices[1])
            arr.pop(remove_indices[0])
            return 1

        return 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.isPossible(N, arr))
# } Driver Code Ends