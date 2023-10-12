class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        
        # Binary search to find the peak element
        left, right = 0, n - 1
        while left < right:
            mid = left + (right - left) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                left = mid + 1
            else:
                right = mid
        
        peak_index = left
        
        # Binary search in the left subarray
        left, right = 0, peak_index
        while left <= right:
            mid = left + (right - left) // 2
            mid_val = mountain_arr.get(mid)
            if mid_val == target:
                return mid
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
        
        # Binary search in the right subarray
        left, right = peak_index, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            mid_val = mountain_arr.get(mid)
            if mid_val == target:
                return mid
            elif mid_val < target:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1

        