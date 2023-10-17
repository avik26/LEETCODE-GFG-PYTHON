class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # Create an array to track the parent of each node.
        parents = [-1] * n

        # Count the indegree of each node, and track the root node.
        indegree = [0] * n
        root = -1

        for i in range(n):
            left = leftChild[i]
            right = rightChild[i]

            if left != -1:
                # If the left child already has a parent, it's not a valid binary tree.
                if parents[left] != -1:
                    return False
                parents[left] = i
                indegree[left] += 1

            if right != -1:
                # If the right child already has a parent, it's not a valid binary tree.
                if parents[right] != -1:
                    return False
                parents[right] = i
                indegree[right] += 1

        # There should be exactly one node with an indegree of 0 to serve as the root.
        for i in range(n):
            if indegree[i] == 0:
                if root == -1:
                    root = i
                else:
                    return False

        if root == -1:
            return False

        # Ensure that there is a single connected component.
        visited = [False] * n

        def dfs(node):
            if node == -1:
                return
            if visited[node]:
                return
            visited[node] = True
            dfs(leftChild[node])
            dfs(rightChild[node])

        dfs(root)

        return all(visited)

# Example usage:
# n = 4, leftChild = [1, 0, 3, -1], rightChild = [-1, -1, -1, -1]
# result = Solution().validateBinaryTreeNodes(n, leftChild, rightChild)
# This will return False for the given example.
