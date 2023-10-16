#User function Template for python3
class Solution:
    def Maximize(self, a, n): 
        mod = 10**9 + 7
        a.sort()
        result = 0
        
        for i in range(n):
            result = (result + (a[i] * i) % mod) % mod
        
        return result



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob=Solution()
    print(ob.Maximize(arr, n))
    
# } Driver Code Ends