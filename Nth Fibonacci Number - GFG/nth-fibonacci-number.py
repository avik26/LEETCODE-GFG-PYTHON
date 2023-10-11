
class Solution:
    def nthFibonacci(self, n: int) -> int:
        # Initialize an array to store the Fibonacci numbers
        fib = [0] * (n + 1)
        
        # Base cases for the first two Fibonacci numbers
        fib[0] = 0
        if n > 0:
            fib[1] = 1
        
        # Calculate Fibonacci numbers from the third to the nth
        for i in range(2, n + 1):
            fib[i] = (fib[i - 1] + fib[i - 2]) % 1000000007
        
        return fib[n]




#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        obj = Solution()
        res = obj.nthFibonacci(n)
        
        print(res)
        

# } Driver Code Ends