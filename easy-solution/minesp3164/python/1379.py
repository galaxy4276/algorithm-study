class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        if not original or original is target:
            return cloned
        return self.getTargetCopy(original.left, cloned.left,target) or self.getTargetCopy(original.right, cloned.right, target)