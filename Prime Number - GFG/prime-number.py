#User function Template for python3

class Solution:
    def isPrime(self, N):
        # If N is less than 2, it's not a prime number
        if N < 2:
            return 0

        # Check for factors from 2 to the square root of N
        for i in range(2, int(N**0.5) + 1):
            if N % i == 0:
                return 0  # N is divisible by i, so it's not prime

        return 1  # N is prime if it's not divisible by any number from 2 to sqrt(N)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.isPrime(N))
# } Driver Code Ends