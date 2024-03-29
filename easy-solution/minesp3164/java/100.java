class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q== null)return true;
        if(q == null || p == null) return false;
        if(q.val != p.val)return false;
        return isSameTree(p.right, q.right) && isSameTree(p.left, q.left);
    }
}