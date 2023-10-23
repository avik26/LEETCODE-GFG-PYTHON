class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # Check if n is a positive power of two
        if n <= 0 or (n & (n - 1)) != 0:
            return False
        
        # Check if the only set bit is at an even position
        return n & 0xAAAAAAAA == 0
