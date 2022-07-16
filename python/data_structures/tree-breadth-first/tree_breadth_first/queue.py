from .queue_node import Node
from .invalid_operation_error import InvalidOperationError


class Queue:
    """
    This class contains the following methods: __init__, enqueue, dequeue, peek, and is_empty.
    """

    def __init__(self, front=None, rear=None):
        self.front = None
        self.rear = None

    def enqueue(self, new_value):
        """
         Adds a new node.

         Args:
             new_value (): value to insert.

         Returns:
             queue: queue with a new node at the rear.
         """
        node = Node(new_value)
        if self.front is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        """

        Returns:
            value: value of the temp node that was removed or raises error
        """
        if self.front is None:
            self.is_empty()
            raise InvalidOperationError("Method not allowed on empty collection")
        else:
            temp = self.front
            print(temp.value)
            self.front = self.front.next
            temp.next = None
            return temp.value

    def peek(self):
        """

        Returns:
            Value: Front value of queue or error message
        """
        if self.front is None:
            self.is_empty()
            raise InvalidOperationError("Method not allowed on empty collection")
        else:
            temp = self.front
            return temp.value

    def is_empty(self):
        """

        Returns:
            Value: Boolean
        """
        if not self.front:
            return True
