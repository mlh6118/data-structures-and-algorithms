from linked_list import Node, LinkedList


class Hashtable:
    def __init__(self, size=1024):
        self.size = size
        self._buckets = size * [None]

    def set(self, key, value):
        """
        Args:
            key:
            value:

        Returns:
            nothing

        This method should hash the key, and add the key and value pair to the table, handling collisions as needed.
        """
        # Call the hash method.
        bucket_index = self.hash(key)

        # Check if the hash value index already has a key:value pair associated to it.
        # self._buckets[bucket_index] IS a Linked List!
        if self._buckets[bucket_index] is None:
            # If no, put the key:value pair in it.
            # node = Node((key, value))
            self._buckets[bucket_index] = LinkedList()
            self._buckets[bucket_index].insert((key, value))
        else:
            # If yes, add the key:value pair to the existing list as the head.
            self._buckets[bucket_index].insert((key, value))

    def get(self, key):
        # Arguments: key
        # Returns: Value associated with that key in the table
        bucket: LinkedList = self._buckets[self.hash(key)]
        if bucket is None:
            return None
        elif bucket.size() == 1:
            return bucket.head.value[1]
        else:
            current = bucket.head
            while current:
                if current.value[0] == key:
                    return current.value[1]
                current = current.next

    def contains(self, key):
        # Arguments: key
        # Returns: Boolean, indicating if the key exists in the table already.
        bucket: LinkedList = self._buckets[self.hash(key)]
        if bucket is None:
            return False
        else:
            current = bucket.head
            while current:
                if current.value[0] == key:
                    return True
                current = current.next
            # If the key is not found, return False.
            return False

    def keys(self):
        # Returns: Collection of keys
        list_of_keys = []
        # Want each bucket in the list.
        for bucket in self._buckets:
            # Need to check if bucket is None.
            if bucket is None:
                continue
            elif bucket is not None:
                # Want each key in the bucket which is a linked list.
                current = bucket.head
                while current:
                    list_of_keys.append(current.value[0])
                    current = current.next
        return list_of_keys

    #     'roger' 10431 list: 1024
    def hash(self, key):
        # hash
        # Arguments: key
        # Returns: Index in the collection for that key

        total = 0

        for ch in key:
            total += ord(ch)

        primed = total * 19

        index = primed % self.size
        return index
