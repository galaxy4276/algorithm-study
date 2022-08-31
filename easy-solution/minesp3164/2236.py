class Solution(object):
    def checkTree(self, root):
        if root.right.val + root.left.val == root.val:
            return True
        return False