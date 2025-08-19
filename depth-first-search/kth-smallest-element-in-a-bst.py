# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        self.res = None
        self.k = k
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            self.k -= 1
            if self.k == 0:
                self.res = node.val
                return
            inorder(node.right)
        inorder(root)
        return self.res
        