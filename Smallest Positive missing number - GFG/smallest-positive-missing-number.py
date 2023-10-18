#User function Template for python3

class Solution:
    def missingNumber(self, arr, n):
        # Separate positive numbers from non-positive numbers
        pos_index = 0
        for i in range(n):
            if arr[i] <= 0:
                arr[i], arr[pos_index] = arr[pos_index], arr[i]
                pos_index += 1
        
        # Consider only positive numbers
        pos_arr = arr[pos_index:]
        m = len(pos_arr)
        
        # Mark the elements present in the array by changing the sign of their
        # corresponding indices to negative
        for i in range(m):
            if abs(pos_arr[i]) <= m:
                pos_arr[abs(pos_arr[i]) - 1] = -abs(pos_arr[abs(pos_arr[i]) - 1])
        
        # Find the first index with a positive value, which corresponds to the
        # smallest missing positive number
        for i in range(m):
            if pos_arr[i] > 0:
                return i + 1
        
        # If all indices are negative, the answer is m + 1
        return m + 1



#{ 
 # Driver Code Starts
#Initial Template for Python 3


import math


def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            print(ob.missingNumber(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends