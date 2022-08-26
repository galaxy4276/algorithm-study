class Solution:
    def diameterOfBinaryTree(self, root):
        self.diameter = 0
        def dfs(root):
            if not root: return 0
            leftLongestPath = dfs(root.left)
            rightLongestPath = dfs(root.right)
            self.diameter = max(self.diameter, (leftLongestPath + rightLongestPath))
            return max(leftLongestPath, rightLongestPath) + 1
        dfs(root)
        return self.diameter