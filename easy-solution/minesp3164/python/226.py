## 이진트리 왼쪽, 오른쪽 바꾸기 in dfs
class Solution(object):
    def invertTree(self, root):
        if not root:
            return None
        
        root.left, root.right = root.right, root.left
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root