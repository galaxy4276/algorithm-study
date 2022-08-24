class Solution {
  public TreeNode searchBST(TreeNode root, int val) {
    if (root == null) return null;
    if (root.val == val) return root;
    TreeNode next = null;
    if (root.val > val) {
      if (root.left != null)
        next = searchBST(root.left, val);
    } else {
      if (root.right != null)
        next = searchBST(root.right, val);
    }

    return next;
  }
}