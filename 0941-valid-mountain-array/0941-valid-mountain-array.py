class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        
        if n < 3:
            return False
        
        # Find the peak of the mountain
        peak = max(arr)
        peak_idx = arr.index(peak)
        
        if peak_idx == 0 or peak_idx == n - 1:
            return False
        
        # Check the left side (strictly increasing)
        for i in range(peak_idx):
            if arr[i] >= arr[i + 1]:
                return False
        
        # Check the right side (strictly decreasing)
        for i in range(peak_idx, n - 1):
            if arr[i] <= arr[i + 1]:
                return False
        
        return True
