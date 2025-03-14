class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if not node:
            return 0
        return node.height

    def balance_factor(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def update_height(self, node):
        if not node:
            return
        node.height = max(self.height(node.left), self.height(node.right)) + 1

    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self.update_height(y)
        self.update_height(x)

        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        self.update_height(x)
        self.update_height(y)

        return y

    def insert(self, value):
        self.root = self._insert_recursively(self.root, value)

    def _insert_recursively(self, node, value):
        if not node:
            return AVLNode(value)

        if value < node.value:
            node.left = self._insert_recursively(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursively(node.right, value)
        else:
            return node

        self.update_height(node)

        balance = self.balance_factor(node)

        # Left Left Case
        if balance > 1 and value < node.left.value:
            return self.right_rotate(node)

        # Right Right Case
        if balance < -1 and value > node.right.value:
            return self.left_rotate(node)

        # Left Right Case
        if balance > 1 and value > node.left.value:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Right Left Case
        if balance < -1 and value < node.right.value:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def display(self):
        lines = self._display_recursive(self.root, 0)
        for line in lines:
            print(line)

    def _display_recursive(self, node, level):
        if node is None:
            return []

        lines = []
        lines.extend(self._display_recursive(node.right, level + 1))
        
        lines.append('   ' * level + f'-> {node.value} (h={node.height})')
        
        lines.extend(self._display_recursive(node.left, level + 1))
        
        return lines

    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

    def get_min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, value):
        self.root = self._delete_recursively(self.root, value)

    def _delete_recursively(self, node, value):
        if not node:
            return None

        if value < node.value:
            node.left = self._delete_recursively(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursively(node.right, value)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children
            successor = self.get_min_value_node(node.right)
            node.value = successor.value
            node.right = self._delete_recursively(node.right, successor.value)

        self.update_height(node)

        balance = self.balance_factor(node)

        # Left Left Case
        if balance > 1 and self.balance_factor(node.left) >= 0:
            return self.right_rotate(node)

        # Left Right Case
        if balance > 1 and self.balance_factor(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Right Right Case
        if balance < -1 and self.balance_factor(node.right) <= 0:
            return self.left_rotate(node)

        # Right Left Case
        if balance < -1 and self.balance_factor(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

if __name__ == "__main__":
    avl_tree = AVLTree()
    
    # Test insertions
    values = [10, 20, 30, 40, 50, 25]
    for value in values:
        avl_tree.insert(value)
        print(f"\nAfter inserting {value}:")
        avl_tree.display()
    
    print("\nInorder traversal:", avl_tree.inorder_traversal())
    
    # Test deletions
    delete_values = [30, 40, 20]
    for value in delete_values:
        avl_tree.delete(value)
        print(f"\nAfter deleting {value}:")
        avl_tree.display()
        print("Inorder traversal:", avl_tree.inorder_traversal())