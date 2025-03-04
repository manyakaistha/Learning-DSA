# the first code only work for trees with depth 1 as asked in leetcode 2236
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        def check_sum(node):
            if not node:
                return True

            left_val = node.left.val if node.left else 0
            right_val = node.right.val if node.right else 0

            return node.val == left_val + right_val

        return check_sum(root)

# code below works for tree of any depth
class Solution_Any_depth:
    def checkTree(self, root):
        def check_sum(node):
            if not node:
                return True

            if not node.left and not node.right:
                return True

            left_val = node.left.val if node.left else 0
            right_val = node.right.val if node.right else 0

            return (node.val == left_val + right_val and check_sum(node.left) and check_sum(node.right))

        return check_sum(root)
