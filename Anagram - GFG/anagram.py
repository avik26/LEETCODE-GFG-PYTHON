#User function Template for python3

class Solution:
    def isAnagram(self, a, b):
        # If the lengths of the two strings are not the same, they can't be anagrams.
        if len(a) != len(b):
            return False
        
        # Create dictionaries to store the character frequency in both strings.
        char_count_a = {}
        char_count_b = {}
        
        # Count the frequency of characters in string a.
        for char in a:
            char_count_a[char] = char_count_a.get(char, 0) + 1
        
        # Count the frequency of characters in string b.
        for char in b:
            char_count_b[char] = char_count_b.get(char, 0) + 1
        
        # Check if the character frequency dictionaries are the same.
        return char_count_a == char_count_b




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        a,b=map(str,input().strip().split())
        if(Solution().isAnagram(a,b)):
            print("YES")
        else:
            print("NO") 
# } Driver Code Ends