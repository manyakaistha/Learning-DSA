class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursively(self.root, value)

    def _insert_recursively(self, node, value):
        if value >= node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursively(node.right, value)
        else:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursively(node.left, value)

    def search(self, value):
        result = self._search_recursively(self.root, value)
        if result:
            print(f"Found value: {result.value}")
        else:
            print(f"Value {value} not found in the tree")
        return result

    def _search_recursively(self, node, value):
        if node is None or node.value == value:
            return node

        if value < node.value:
            return self._search_recursively(node.left, value)
        else:
            return self._search_recursively(node.right, value)

    def preorder_traversal(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

    def postorder_traversal(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)

    def depth(self, value):
        result = self._depth_recursively(self.root, value, 0)
        return result

    def _depth_recursively(self, node, value, dept):
        if node == None:
            return -1

        if node.value == value:
            return dept

        if value < node.value:
            return self._depth_recursively(node.left, value, dept + 1)
        else:
            return self._depth_recursively(node.right, value, dept + 1)

    def display(self):
        lines = self._display_recursive(self.root, 0)
        for line in lines:
            print(line)

    def _display_recursive(self, node, level):
        if node is None:
            return []

        lines = []
        # Recursively get right subtree lines first
        lines.extend(self._display_recursive(node.right, level + 1))

        # Add current node
        lines.append('   ' * level + f'-> {node.value}')

        # Then get left subtree lines
        lines.extend(self._display_recursive(node.left, level + 1))

        return lines

if __name__ == "__main__":
    tree = BinaryTree()

    # Insert some values
    values = [5, 3, 7, 1, 4, 6, 8]
    for value in values:
        tree.insert(value)

    tree.search(6)
    tree.search(0)
    tree.display()
    print(tree.preorder_traversal())
    print(tree.inorder_traversal())
    print(tree.postorder_traversal())
    print(tree.depth(6))
