#User function Template for python3

class Solution:
    def subArrayExists(self, arr, n):
        # Initialize a set to store the prefix sums.
        prefix_sum_set = set()
        prefix_sum = 0

        for num in arr:
            prefix_sum += num

            # If the current prefix sum is 0 or has been seen before, there is a subarray with a sum of 0.
            if prefix_sum == 0 or prefix_sum in prefix_sum_set:
                return True

            # Add the current prefix sum to the set.
            prefix_sum_set.add(prefix_sum)

        # If we have gone through the entire array without finding a subarray with sum 0, return False.
        return False



#{ 
 # Driver Code Starts
#Initial Template for Python 3



def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        if(Solution().subArrayExists(arr,n)):
            print("Yes")
        else:
            print("No")
        
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends