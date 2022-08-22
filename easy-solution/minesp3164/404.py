class Solution:
    def sumOfLeftLeaves(self, root) -> int:
        def solver(r,s,parity):
            if not r:
                return 0
            if not r.left and not r.right and parity==1:
                s+=r.val
                return s
            return(solver(r.left,s,1)+solver(r.right,s,0))
        return solver(root,0,0)