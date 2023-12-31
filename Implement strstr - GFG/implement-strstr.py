#Function to locate the occurrence of the string x in the string s.
def strstr(s, x):
    s_len = len(s)
    x_len = len(x)

    for i in range(s_len - x_len + 1):
        j = 0

        # Check if the substring x matches s starting at position i
        while j < x_len and s[i + j] == x[j]:
            j += 1

        # If all characters in x match s starting at position i, return the index
        if j == x_len:
            return i

    # If no match is found, return -1
    return -1

#{ 
 # Driver Code Starts
#Contributed by : Nagendra Jha

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        s,p =input().strip().split()
        print(strstr(s,p))


# } Driver Code Ends