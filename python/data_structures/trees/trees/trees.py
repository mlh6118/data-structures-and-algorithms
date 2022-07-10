class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f"Node {self.value}"


class BinaryTree:
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

        def walk(node, value):

            print(self.root)

            if not self.root:
                return

            print(node.value)
            print(value)

            if node.value > value:
                walk(node.left, value)
            elif node.value < value:
                walk(node.right, value)
            elif node.value == value:
                return True

        walk(self.root, value)
