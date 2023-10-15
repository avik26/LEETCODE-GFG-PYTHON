#User function Template for python3

def rotate(arr, n):
    if n <= 1:
        return arr  # No rotation needed for arrays with 0 or 1 element

    # Step 1: Store the last element in a temporary variable
    temp = arr[n - 1]

    # Step 2 and 3: Move elements to the right
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]

    # Step 4: Assign the value from the temporary variable to the first element
    arr[0] = temp

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        rotate(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends