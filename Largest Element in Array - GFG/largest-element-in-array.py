#User function Template for python3

def largest(arr, n):
    if n == 0:
        return None  # Handle the case of an empty array.

    max_element = arr[0]  # Initialize max_element with the first element of the array.

    for i in range(1, n):
        if arr[i] > max_element:
            max_element = arr[i]

    return max_element



#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        print(largest(a, n))

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends