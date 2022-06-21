from stacks_and_queues.node import Node
from stacks_and_queues.invalid_operation_error import InvalidOperationError


class Stack:
    """
    This class contains the following methods: __init__, push, pop, is_empty, peek
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
            value: value of the temp node that was removed or raises error
        """
        if self.top is None:
            self.is_empty()
            raise InvalidOperationError("Method not allowed on empty collection")
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp.value

    def is_empty(self):
        """

        Returns:
            Value: Boolean
        """
        if not self.top:
            return True

    def peek(self):
        """

        Returns:
            Value: Top value of stack or error message
        """
        if self.top:
            return self.top.value
        else:
            raise InvalidOperationError("Method not allowed on empty collection")


class PseudoQueue(Stack):

    def enqueue(self, new_value):
        temp_stack = PseudoQueue()
        while not self.is_empty():
            temp_stack.push(self.pop())
        self.push(new_value)
        while not temp_stack.is_empty():
            self.push(temp_stack.pop())

    def dequeue(self):
        print(self.top.value)
        if not self.is_empty():
            return self.pop()
