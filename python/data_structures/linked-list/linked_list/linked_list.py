class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        return self.to_string()

    def insert(self, value):
        node = Node(value)
        if self.head is not None:
            node.next = self.head
        self.head = node

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def to_string(self):
        new_str = ""
        current = self.head
        while current:
            new_str += "{ " + str(current.value) + " } -> "
            current = current.next
        new_str += "NULL"
        return new_str

    def append(self, new_value):
        '''
        This method will add a new node to the end of a linked list.  If there are no nodes in the linked list,
        the method will call the insert method to add the node.
        '''
        if self.head is None:
            self.insert(new_value)
            return
        current = self.head
        while current:
            if current.next is None:
                node = Node(new_value)
                current.next = node
                return
            current = current.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert(5)
    ll.insert(6)
    ll.insert(7)
    ll.to_string()
