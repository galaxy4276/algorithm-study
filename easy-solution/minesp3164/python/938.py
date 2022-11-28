class Solution(object):
    def rangeSumBST(self, root, low, high):
        def dfs(node):
            if not node:
                return 0

            if node.val < low:
                return dfs(node.right)
            elif node.val > high:
                return dfs(node.left)
            else:
                return node.val + dfs(node.left) + dfs(node.right)

        return dfs(root)
