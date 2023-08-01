# Maximum Depth of N-ary Tree

class Solution(object):
  def maxDepth(self, root):
    if not root: return 0
    return 1 + max(map(self.maxDepth, root.children or [None]))