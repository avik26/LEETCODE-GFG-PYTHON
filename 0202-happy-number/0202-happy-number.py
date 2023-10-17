class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(num):
            total_sum = 0
            while num > 0:
                num, digit = divmod(num, 10)
                total_sum += digit ** 2
            return total_sum

        slow = n
        fast = n

        while True:
            slow = get_next(slow)  # Move one step.
            fast = get_next(get_next(fast))  # Move two steps.

            if fast == 1:
                return True  # If fast reaches 1, it's a happy number.
            if slow == fast:
                return False  # If there's a cycle (other than 1), it's not a happy number.

# Example usage:
# n = 19
# result = Solution().isHappy(n)
# This will return True for the given example.
