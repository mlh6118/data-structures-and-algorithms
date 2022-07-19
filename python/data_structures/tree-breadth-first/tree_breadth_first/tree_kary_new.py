from .queue import Queue
from .kary_tree import KaryTree, Node


def fizz_buzz_tree(self):
    new_tree = KaryTree()
    queue = Queue()

    if not self.root:
        return "The tree is empty."

    if self.root:
        queue.enqueue(self.root)

        while not queue.is_empty():
            dequeued = queue.dequeue()

            for child in dequeued.children:
                queue.enqueue(child)

            value_string = ' '

            if dequeued.value % 3 == 0:
                value_string += "fizz"
            if dequeued.value % 5 == 0:
                value_string += "buzz"
            if dequeued.value % 3 != 0 and dequeued.value % 5 != 0:
                value_string = str(dequeued.value)

            new_node = Node(value_string)
            new_tree.root.children.append(new_node)

    return new_tree
