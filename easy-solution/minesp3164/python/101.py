class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return true;
        return self.isSame(root.left, root.right)

    def isSame(self, leftroot, rightroot):
        if leftroot == None and rightroot == None:
            return True
        if leftroot == None or rightroot == None:
            return False
        if leftroot.val != rightroot.val:
            return False
        return self.isSame(leftroot.left, rightroot.right) and self.isSame(leftroot.right, rightroot.left)