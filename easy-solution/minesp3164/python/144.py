# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        answer = []

        def dfs(node):
            if not node:
                return
            answer.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return answer