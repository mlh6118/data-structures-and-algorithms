from .queue import Queue


def breadth_first(self):
    """
    Returns:
        list: a list of the node values.
    """

    breadth_first_queue = Queue()

    values_list = []

    if self.root:
        breadth_first_queue.enqueue(self.root)
        while not breadth_first_queue.is_empty():
            dequeued_node = breadth_first_queue.dequeue()
            if dequeued_node.left:
                breadth_first_queue.enqueue(dequeued_node.left)
            if dequeued_node.right:
                breadth_first_queue.enqueue(dequeued_node.right)
            values_list.append(dequeued_node.value)

    return values_list
