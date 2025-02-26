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
           return result
        else:
            return -1

    def _search_recursively(self, node, value):
        if node is None or node.value == value:
            return node

        if value < node.value:
            return self._search_recursively(node.left, value)
        else:
            return self._search_recursively(node.right, value)

    # DFS based traversal
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

    # BFS/Level Order Travarsal
    def level_order_traversal(self):
        if not self.root:
            return []

        result = []
        queue = [(self.root, 0)]

        while queue:
            current, level = queue.pop(0)
            if len(result) == level:
                result.append([])

            result[level].append(current.value)

            if current.left:
                queue.append((current.left, level + 1))

            if current.right:
                queue.append((current.right, level + 1))

        return result

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

    def height(self, value=None):
        if value is None:
            return self._height_recursively(self.root)
        else:
            node = self.search(value)
            if node is None:
                return -1
            return self._height_recursively(node)

    def _height_recursively(self, node):
        if node == None:
            return -1

        left_height = self._height_recursively(node.left)
        right_height = self._height_recursively(node.right)

        return max(left_height, right_height) + 1

    def display(self):
        lines = self._display_recursive(self.root, 0)
        for line in lines:
            print(line)

    def get_min(self):
        if self.root == None:
            return None
        return self._get_min_recursively(self.root)
   # this only works because this is a binary serch tree and the node are sorted
    def _get_min_recursively(self, node):
        if node.left is None:
            return node.value
        return self._get_min_recursively(node.left)

    def is_identical(self, other_tree):
        return self._is_identical_recursively(self.root, other_tree.root)

    def _is_identical_recursively(self, node1, node2):
        if node1 is None and node2 is None:
            return True

        if node1 is None or node2 is None:
            return False

        return (node1.value == node2.value and
            self._is_identical_recursively(node1.left, node2.left) and
            self._is_identical_recursively(node1.right, node2.right))

    def _display_recursive(self, node, level):
        if node is None:
            return []

        lines = []
        lines.extend(self._display_recursive(node.right, level + 1))

        lines.append('   ' * level + f'-> {node.value}')

        lines.extend(self._display_recursive(node.left, level + 1))

        return lines

if __name__ == "__main__":
    tree1 = BinaryTree()
    values1 = [5, 3, 7, 1, 4, 6, 8]
    for value in values1:
        tree1.insert(value)

    tree2 = BinaryTree()
    values2 = [5, 3, 7, 1, 4, 6, 8]
    for value in values2:
        tree2.insert(value)

    tree3 = BinaryTree()
    values3 = [5, 3, 7, 1, 4, 6, 9]
    for value in values3:
        tree3.insert(value)

    tree1.search(6)
    tree1.search(0)
    tree1.search(3)
    tree1.display()
    print(tree1.preorder_traversal())
    print(tree1.inorder_traversal())
    print(tree1.postorder_traversal())
    print(tree1.depth(6))
    print(tree1.height())
    print(tree1.get_min())
    print(tree1.is_identical(tree2))
    print(tree3.is_identical(tree2))
