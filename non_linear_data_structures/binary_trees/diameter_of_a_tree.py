#this is is sovled by finding the maximum height form each node

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        diameter = 0

        def height(node):
            left_height, right_height = 0, 0

            if node.left is not None:
                left_height = height(node.left)
            if node.right is not None:
                right_height = height(node.right)

            nonlocal diameter
            diameter = max(diameter, left_height + right_height)

            return 1 + max(left_height, right_height)

        height(root)

        return diameter
