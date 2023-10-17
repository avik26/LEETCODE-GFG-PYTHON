from collections import Counter

class Solution:
    def topK(self, nums, k):
        # Count the frequency of each element using Counter
        freq_counter = Counter(nums)

        # Sort elements based on frequency and value
        sorted_elements = sorted(set(nums), key=lambda x: (-freq_counter[x], -x))

        # Get the top k elements
        top_k = sorted_elements[:k]

        return top_k


#{ 
 # Driver Code Starts
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	a = list(map(int, input().strip().split()))
    	n = a[0]
    	nums = a[1:]
    	k = int(input().strip())
    	obj = Solution()
    	ans = obj.topK(nums, k)
    	for i in ans:
    		print(i, end = " ")
    	print()
    	
# } Driver Code Ends