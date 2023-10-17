#User function Template for python3

class Solution:
    def eventualSafeNodes(self, V, adj):
        def isSafe(node):
            if visited[node] == 1:
                return True
            if visited[node] == -1:
                return False
            visited[node] = -1
            for neighbor in adj[node]:
                if not isSafe(neighbor):
                    return False
            visited[node] = 1
            return True

        visited = [0] * V
        safe_nodes = []

        for node in range(V):
            if isSafe(node):
                safe_nodes.append(node)

        return safe_nodes

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T = int(input())
    for t in range(T):
        
        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v = map(int, input().strip().split())
            adj[u].append(v)
        obj = Solution()
        ans = obj.eventualSafeNodes(V, adj)
        for nodes in ans:
            print(nodes, end = ' ')
        print()
            


# } Driver Code Ends