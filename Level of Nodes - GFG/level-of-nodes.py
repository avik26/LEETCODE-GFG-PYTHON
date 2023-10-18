#User function Template for python3

from collections import deque

class Solution:
    # Function to find the level of node X.
    def nodeLevel(self, V, adj, X):
        # Create a list to keep track of visited nodes.
        visited = [False] * V
        # Create a queue for BFS.
        queue = deque()
        # Initialize the level of node 0 to 0.
        level = 0

        # Start BFS from node 0.
        queue.append(0)
        visited[0] = True

        while queue:
            # Get the number of nodes at this level.
            num_nodes_at_level = len(queue)

            # Process all nodes at the current level.
            for i in range(num_nodes_at_level):
                node = queue.popleft()

                # Check if the current node is the one we are looking for.
                if node == X:
                    return level

                # Add unvisited neighbors to the queue.
                for neighbor in adj[node]:
                    if not visited[neighbor]:
                        queue.append(neighbor)
                        visited[neighbor] = True

            # Increment the level for the next iteration.
            level += 1

        # If X is not found, return -1.
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
            adj[b].append(a)
        X=int(input())
        ob = Solution()
        
        print(ob.nodeLevel(V, adj, X))
# } Driver Code Ends