#User function Template for python3

class Solution:
    # Function to return a list containing the first n Fibonacci numbers.
    def printFibb(self, n):
        # Initialize a list to store the Fibonacci numbers
        fibonacci_numbers = []

        # Initialize the first two numbers in the sequence
        a, b = 1, 1

        # Loop to generate Fibonacci numbers and append them to the list
        for i in range(n):
            fibonacci_numbers.append(a)
            a, b = b, a + b

        return fibonacci_numbers

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        
        n=int(input())
        res = Solution().printFibb(n)
        for i in range (len(res)):
            print (res[i], end = " ") 
        print()
# } Driver Code Ends