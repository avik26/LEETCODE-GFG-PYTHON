#User function Template for python3

class Solution:
    def check(self, A, B, N):
        # Check if the lengths of the arrays are the same
        if len(A) != len(B):
            return False
        
        # Create dictionaries to count the occurrences of elements in both arrays
        count_A = {}
        count_B = {}
        
        # Count occurrences in array A
        for num in A:
            if num in count_A:
                count_A[num] += 1
            else:
                count_A[num] = 1
        
        # Count occurrences in array B
        for num in B:
            if num in count_B:
                count_B[num] += 1
            else:
                count_B[num] = 1
        
        # Check if the dictionaries are equal
        return count_A == count_B


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        N=int(input())
        
        A = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        B = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        ob=Solution()
        if ob.check(A,B,N):
            print(1)
        else:
            print(0)
        
                
                
# } Driver Code Ends