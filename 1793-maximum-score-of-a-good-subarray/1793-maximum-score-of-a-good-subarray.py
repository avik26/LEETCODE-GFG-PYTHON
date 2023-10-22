class Solution:
    def maximumScore(self, nums, k):
        n = len(nums)
        left, right = k, k
        score = nums[k]
        max_score = score

        while score > 0:
            while left > 0 and nums[left - 1] >= score:
                left -= 1
            while right < n - 1 and nums[right + 1] >= score:
                right += 1
            max_score = max(max_score, score * (right - left + 1))

            if left == 0 and right == n - 1:
                break
            elif left == 0:
                right += 1
                score = nums[right]
            elif right == n - 1:
                left -= 1
                score = nums[left]
            else:
                if nums[left - 1] > nums[right + 1]:
                    left -= 1
                    score = nums[left]
                else:
                    right += 1
                    score = nums[right]

        return max_score