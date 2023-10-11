#User function Template for python3
class Solution:
    def rotateArr(self, A, D, N):
        # Function to reverse the elements of the array in the specified range.
        def reverse(arr, start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
        
        # Handle the case where D is greater than the array size
        D = D % N
        
        # Reverse the first D elements
        reverse(A, 0, D - 1)
        
        # Reverse the remaining N - D elements
        reverse(A, D, N - 1)
        
        # Reverse the entire array
        reverse(A, 0, N - 1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
def main():
    T=int(input())
    
    while(T>0):
        nd=[int(x) for x in input().strip().split()]
        N=nd[0]
        D=nd[1]
        A=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.rotateArr(A,D,N)
        
        for i in A:
            print(i,end=" ")
            
        print()
       
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends