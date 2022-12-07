class Solution(object):
    def sumRootToLeaf(self, root):
        def tree(node, num):
            if not node :
                return 0

            num = (num *2) + node.val
            if not node.left and not node.right:
                return num
            return tree(node.left, num) + tree(node.right, num)

        return tree(root, 0)

## Solution!
# class Solution:
#     def sumRootToLeaf(self, root: TreeNode) -> int:
#         def preorder(r, curr_number):
#             nonlocal root_to_leaf
#             if r:
#                 curr_number = (curr_number << 1) | r.val
#                 # if it's a leaf, update root-to-leaf sum
#                 if not (r.left or r.right):
#                     root_to_leaf += curr_number
#
#                 preorder(r.left, curr_number)
#                 preorder(r.right, curr_number)
#
#         root_to_leaf = 0
#         preorder(root, 0)
#         return root_to_leaf