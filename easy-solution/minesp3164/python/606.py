# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree2str(self, root):
        def dfs(root):
            if not root:
                return ''

            left = dfs(root.left)
            right = dfs(root.right)

            if (root.left or root.right) and not left:
                left = "()"
            return '(' + str(root.val) + left + right + ')'

        return dfs(root)[1: -1]