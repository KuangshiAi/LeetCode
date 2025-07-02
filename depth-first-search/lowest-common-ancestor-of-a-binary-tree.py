# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        
        def search(root, p, q):
            if root == q or root == p or not root:
                return root
            left = search(root.left, p, q)
            right = search(root.right, p, q)
            if left and right:
                return root
            if not left:
                return right
            if not right:
                return left
        return search(root, p, q)
        