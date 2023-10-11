#User function Template for python3
class Solution:
    def isPalindrome(self, S):
        # Convert the string to lowercase and remove non-alphanumeric characters
        S = ''.join(c for c in S if c.isalnum()).lower()
        
        # Initialize two pointers, one at the beginning and one at the end
        left, right = 0, len(S) - 1
        
        while left < right:
            # Compare characters at the left and right positions
            if S[left] != S[right]:
                return 0  # Not a palindrome
            left += 1
            right -= 1
        
        return 1  # It is a palindrome


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.isPalindrome(S)
		print(answer)

# } Driver Code Ends