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
        return self._search_recursively(self.root, value)

    def _search_recursively(self, node, value):
        if node is None or node.value == value:
            return node

        if value < node.value:
            return self._search_recursively(node.left, value)
        else:
            return self._search_recursively(node.right, value)


    def display(self):
        def _display_recursive(node, level=0, prefix="Root: "):
            if node is not None:
                print("  " * level + prefix + str(node.value))
                if node.left or node.right:
                    if node.left:
                        _display_recursive(node.left, level + 1, "L--- ")
                    if node.right:
                        _display_recursive(node.right, level + 1, "R--- ")

        _display_recursive(self.root)

if __name__ == "__main__":
    tree = BinaryTree()

    # Insert some values
    values = [5, 3, 7, 1, 4, 6, 8]
    for value in values:
        tree.insert(value)

    tree.display()
