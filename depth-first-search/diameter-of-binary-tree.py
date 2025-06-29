# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.ans = 1
        def diam(node):
            if not node:
                return 0
            L = diam(node.left)
            R = diam(node.right)
            self.ans = max(self.ans, L+R)
            return max(L,R) + 1
        diam(root)
        return self.ans
        