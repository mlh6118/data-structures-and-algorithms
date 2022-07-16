class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f"Node {self.value}"


class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        def walk(root):
            if not root:
                return
            values.append(root.value)
            walk(root.left)
            walk(root.right)

        values = []
        walk(self.root)
        return values

    def in_order(self):
        def walk(root):
            if not root:
                return
            walk(root.left)
            values.append(root.value)
            walk(root.right)

        values = []
        walk(self.root)
        return values

    def post_order(self):
        def walk(root):
            if not root:
                return
            walk(root.left)
            walk(root.right)
            values.append(root.value)

        values = []
        walk(self.root)
        return values

    def find_maximum_value(self):
        if not self.root:
            return

        max_value = self.root.value
        tree_values = self.pre_order()

        print(tree_values)

        for value in tree_values:
            if value > max_value:
                max_value = value

        return max_value


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        node = Node(value)

        if not self.root:
            self.root = node
            return

        def walk(root, node):
            if not root:
                return

            if node.value < root.value:
                if root.left:
                    walk(root.left, node)
                else:
                    root.left = node
            else:
                if root.right:
                    walk(root.right, node)
                else:
                    root.right = node

        walk(self.root, node)

    def contains(self, value):
        if not self.root:
            return False

        def walk(root, node):
            if not root:
                return False

            if root.value == value:
                return True
            elif root.value > value:
                return walk(root.left, node)
            else:
                return walk(root.right, node)

        return walk(self.root, value)
