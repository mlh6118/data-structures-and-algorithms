from stacks_and_queues.node import Node


class Stack:
    """
    Put docstring here
    """

    def __init__(self, top=None):
        self.top = top

    def push(self, new_value):
        """
        Adds a new node.

        Args:
            new_value (): value to insert.

        Returns:
            stack: stack with a new top node.
        """
        node = Node(new_value)
        node.next = self.top
        self.top = node

    def pop(self):
        """

        Returns:
            value: value of the temp node that was removed
        """
        if self.top is None:
            self.is_empty()
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp.value

    @staticmethod
    def is_empty():
        return True

