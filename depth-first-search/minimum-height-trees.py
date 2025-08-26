from collections import deque
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n <=2:
            return list(range(n))
        adj = [[] for _ in range(n)]
        degree = [0] * n
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
            degree[i] += 1
            degree[j] += 1
        leaves = deque([i for i in range(n) if degree[i]==1])
        remains = n
        while remains > 2:
            layer_size = len(leaves)
            remains -= layer_size
            for _ in range(layer_size):
                leaf = leaves.popleft()
                for neighbor in adj[leaf]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        leaves.append(neighbor)
        return list(leaves)

        
        