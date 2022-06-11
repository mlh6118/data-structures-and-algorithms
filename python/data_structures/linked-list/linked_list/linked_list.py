class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        """
        Calls to_string method.

        Returns: to_string() results

        """
        return self.to_string()

    def insert(self, value):
        """
        Inserts a new node.

        Args:
            value (): value to insert.

        Returns: N/A

        """
        node = Node(value)
        if self.head is not None:
            node.next = self.head
        self.head = node

    def includes(self, value):
        """
        Checks if value is in linked list.

        Args:
            value (): value to check if in the linked list.

        Returns: Boolean

        """
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def to_string(self):
        """
        Converts linked list to a string.

        Returns: new_str

        """
        new_str = ""
        current = self.head
        while current:
            new_str += "{ " + str(current.value) + " } -> "
            current = current.next
        new_str += "NULL"
        return new_str

    def append(self, new_value):
        """
        Adds new node to end of linked list.

        Args:
            new_value (): value to insert.

        Returns: N/A
        """
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

    def insert_before(self, search_value, new_value):
        """
        Adds new node before a searched value.

        Args:
            search_value (): value to insert new value before.
            new_value (): value to insert.

        Returns: N/A

        Raises: TargetError(Exception)

        """
        if self.head is None:
            self.insert(new_value)
        current = self.head
        if current.next is None:
            if current.value == search_value:
                self.insert(new_value)
                '''
                If search_value is not found, raise an exception.
                '''
            else:
                raise TargetError(Exception)
            return
        while current.next is not None:
            if current.next.value == search_value:
                node = Node(new_value)
                node.next = current.next
                current.next = node
                return
            current = current.next

        '''
        If search_value is not found, raise an exception.
        '''
        raise Exception

    def insert_after(self, search_value, new_value):
        """
        Adds new node after searched value.

        Args:
            search_value (): value to insert new value after.
            new_value (): value to insert.

        Returns: N/A

        Raises: TargetError(Exception)

        """
        if self.head is None:
            self.insert(new_value)
        current = self.head
        if current.next is None:
            if current.value == search_value:
                self.insert(new_value)
                '''
                If search_value is not found, raise an exception.
                '''
            else:
                raise TargetError(Exception)
            return
        while current is not None:
            if current.value == search_value:
                node = Node(new_value)
                node.next = current.next
                current.next = node
                return
            current = current.next

        '''
        If search_value is not found, raise an exception.
        '''
        raise Exception

    def insert_before_empty(self, search_value, new_value):
        """

        Args:
            search_value (): value to insert new value before.
            new_value (): value to insert.

        Returns: N/A

        Raises: TargetError(Exception)

        """
        try:
            self.insert_before(search_value, new_value)
        except TargetError(Exception):
            message = "Cannot insert before an empty linked list."
            raise TargetError(message)

    def insert_before_missing(self, search_value, new_value):
        """

        Args:
            search_value (): value to insert new value before.
            new_value (): value to insert.

        Returns: N/A

        Raises: TargetError(Exception)

        """
        try:
            self.insert_before(search_value, new_value)
        except TargetError(Exception):
            message = "Value to insert before does not exist."
            raise TargetError(message)

    def insert_after_empty(self, search_value, new_value):
        """

        Args:
            search_value (): value to insert new value after.
            new_value (): value to insert.

        Returns: N/A

        Raises: TargetError(Exception)

        """
        try:
            self.insert_after(search_value, new_value)
        except TargetError(Exception):
            message = "Cannot insert after an empty linked list."
            raise TargetError(message)

    def insert_after_missing(self, search_value, new_value):
        """

        Args:
            search_value (): value to insert new value after.
            new_value (): value to insert.

        Returns: N/A

        Raises: TargetError(Exception)

        """
        try:
            self.insert_before(search_value, new_value)
        except TargetError(Exception):
            message = "Value to insert after does not exist."
            raise TargetError(message)


class TargetError(Exception):
    def __init__(self, message):
        super().__init__(message)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert(5)
    ll.insert(6)
    ll.insert(7)
    ll.to_string()
