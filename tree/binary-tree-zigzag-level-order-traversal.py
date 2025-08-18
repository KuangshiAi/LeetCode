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
        level = 0
        while queue:
            n = len(queue)
            cur_layer = deque()
            for i in range(n):
                cur_node = queue.popleft()
                if level % 2 == 0:
                    cur_layer.append(cur_node.val)
                else:
                    cur_layer.appendleft(cur_node.val)
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            res.append(list(cur_layer))
            level += 1
        return res