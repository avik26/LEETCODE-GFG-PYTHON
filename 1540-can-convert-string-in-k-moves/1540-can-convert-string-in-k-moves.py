class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        
        shift_count = [0] * 26  # An array to store the number of shifts needed for each possible shift
        
        for i in range(len(s)):
            diff = (ord(t[i]) - ord(s[i]) + 26) % 26  # Calculate the shift, considering wrapping
            if diff != 0:
                shift_count[diff] += 1
                
                # Check if the total shift is within the allowed limit
                if diff + (shift_count[diff] - 1) * 26 > k:
                    return False
        
        return True
