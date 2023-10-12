#User function Template for python3

class Solution:
    # Function to return the count of the number of elements in the union of two arrays.
    def doUnion(self, a, n, b, m):
        # Create sets from the input arrays to automatically remove duplicates.
        set_a = set(a)
        set_b = set(b)
        
        # Take the union of the two sets to get distinct elements.
        union_set = set_a.union(set_b)
        
        # Return the count of elements in the union set.
        return len(union_set)

# Example usage:

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n,m=[int(x) for x in input().strip().split()]
        
        a=[int(x) for x in input().strip().split()]
        b=[int(x) for x in input().strip().split()]
        ob=Solution()
        
        print(ob.doUnion(a,n,b,m))
# } Driver Code Ends