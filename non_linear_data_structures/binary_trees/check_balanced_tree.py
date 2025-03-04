# we do a botton up approact to check the balance
# we check the balace of the leaf nodes but we also take the height of the nodes and use that to check if the paretn node is balanced

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root):
    def check_height(node):
        if not node:
            return 0

        left_height = check_height(node.left)
        if left_height == -1:
            return -1

        right_height = check_height(node.right)
        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return max(left_height, right_height) + 1

    return check_height(root) != -1

def isBalancedSimple(root):
    def check_height(node):
        if not node:
            return [True, 0]

        left_height = check_height(node.left)
        right_height = check_height(node.right)

        balance = (left_height[0] and right_height[0] and abs(left_height[1] - right_height[1]) <= 1)

        return [balance, 1 + max(left_height[1], right_height[1])]
    return check_height(root)[0]
