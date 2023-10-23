#User function Template for python3

class Solution:
    def palindromicPartition(self, string):
        n = len(string)
        
        # Create a table to store whether substrings are palindromes
        is_palindrome = [[False] * n for _ in range(n)]

        # Initialize the table for single characters (all are palindromes)
        for i in range(n):
            is_palindrome[i][i] = True

        # Calculate whether substrings are palindromes
        for cl in range(2, n + 1):
            for i in range(n - cl + 1):
                j = i + cl - 1
                if cl == 2 and string[i] == string[j]:
                    is_palindrome[i][j] = True
                elif string[i] == string[j] and is_palindrome[i + 1][j - 1]:
                    is_palindrome[i][j] = True

        # Create a table to store the minimum cuts required
        dp = [float('inf')] * n

        for i in range(n):
            if is_palindrome[0][i]:
                dp[i] = 0
            else:
                for j in range(i):
                    if is_palindrome[j + 1][i]:
                        dp[i] = min(dp[i], dp[j] + 1)

        # The minimum number of cuts required to partition
        # the entire string into palindromic substrings is stored at dp[n-1]
        return dp[n - 1]
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        string = input()
        
        ob = Solution()
        print(ob.palindromicPartition(string))
# } Driver Code Ends