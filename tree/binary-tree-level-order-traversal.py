# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        que = deque()
        res = []
        if root is None:
            return res
        que.append(root)
        def level_bfs(node):
            while que:
                n = len(que)
                cur_level = []
                for i in range(n):

                    cur = que.popleft()
                    
                    cur_level.append(cur.val)
                    if cur.left:
                        que.append(cur.left)
                    if cur.right:
                        que.append(cur.right)
                res.append(cur_level)
        level_bfs(root)
        return res

        