#User function Template for python3
class Solution:
    def transitiveClosure(self, N, graph):
        # Initialize the transitive matrix with all 0s
        transitive = [[0] * N for _ in range(N)]

        # Copy the input graph to the transitive matrix
        for i in range(N):
            for j in range(N):
                transitive[i][j] = graph[i][j]
                if i == j:
                    transitive[i][j] = 1

        # Perform the transitive closure algorithm
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    if transitive[i][k] and transitive[k][j]:
                        transitive[i][j] = 1

        return transitive


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        graph = []
        for i in range(0,N):
            graph.append([int(j) for j in input().split()])
        ob = Solution()
        ans = ob.transitiveClosure(N, graph)
        for i in range(N):
            for j in range(N):
                print(ans[i][j], end = " ")
            print()
# } Driver Code Ends