class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        kMod = 1_000_000_007
        ans = 0
        prefix = 0
        positions = []

        for num, c in zip(nums, s):
            if c == 'L':
                positions.append(num - d)
            else:
                positions.append(num + d)

        positions.sort()

        for i, p in enumerate(positions):
            ans = ((ans + i * p - prefix) % kMod + kMod) % kMod
            prefix = ((prefix + p) % kMod + kMod) % kMod

        return ans
