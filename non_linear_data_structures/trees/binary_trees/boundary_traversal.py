class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def get_leaves(root):
    leaves = []
    def get_leaves_recursively(node):
        if node:
            if not node.left and not node.right:
                #this prevents double counting in result in a situation where we only have one node i.e root node
                if node != root and node != root.left and node != root.right:
                    leaves.append(node.val)
            else:
                get_leaves_recursively(node.left)
                get_leaves_recursively(node.right)
    get_leaves_recursively(root)
    return leaves

#first append then traverse
def get_left_boundary(root):
    left_boundary = []
    def get_left_boundary_recursively(node):
        if node:
            if node.left or node.right:
                left_boundary.append(node.val)
                if node.left:
                    get_left_boundary_recursively(node.left)
                elif node.right:
                    get_left_boundary_recursively(node.right)

    get_left_boundary_recursively(root.left)
    return left_boundary

#first traverse then appned so i dont need to reverse the array later as recursion is a stack
def get_right_boundary(root):
    right_boundary = []
    def get_right_boundary_recursively(node):
        if node:
            if node.left or node.right:
                if node.right:
                    get_right_boundary_recursively(node.right)
                elif node.left:
                    get_right_boundary_recursively(node.left)
                right_boundary.append(node.val)

    get_right_boundary_recursively(root.right)
    return right_boundary

def boundary_traversal(root):
    result = []
    if root:
        # Add the root node
        result.append(root.val)

        # Get left boundary in top down manner
        result.extend(get_left_boundary(root))

        # Get all leaf nodes
        result.extend(get_leaves(root))

        # Get right boundary in bottom up manner
        result.extend(get_right_boundary(root))

    return result
