from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = deque()
        queue.append(root)
        res = []
        visited = set()
        visited.add(root)
        while len(queue) > 0:
            layer = deque()
            for _ in range(len(queue)):
                node = queue.popleft()
                if len(res) % 2 == 0:
                    layer.append(node.val)
                else:
                    layer.appendleft(node.val)
                if node.left and node.left not in visited:
                    queue.append(node.left)
                if node.right and node.right not in visited:
                    queue.append(node.right)
            res.append(list(layer))
        return res