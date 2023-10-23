class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        if (n & (n - 1)) == 0 and (n & 0x55555555) == n:
            return True
        return False
