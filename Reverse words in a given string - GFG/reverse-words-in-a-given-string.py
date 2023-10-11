# User function Template for python3

class Solution:
    def reverseWords(self, S):
        # Split the input string into words using the dot as a separator
        words = S.split('.')
        
        # Reverse the list of words
        reversed_words = words[::-1]
        
        # Join the reversed words back into a string using the dot as a separator
        reversed_string = '.'.join(reversed_words)
        
        return reversed_string

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        print(obj.reverseWords(s))

# } Driver Code Ends