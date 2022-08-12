# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, nval):
        while root:
            if root.val == nval:
                break
            elif root.val < nval:
                root = root.right
            else: root = root.left
        return root

        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
