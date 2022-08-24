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
        if self._buckets[bucket_index] is None:
            # If no, put the key:value pair in it.
            # node = Node((key, value))
            self._buckets[bucket_index] = LinkedList()
            self._buckets[bucket_index].insert((key, value))
            # return self._buckets[bucket_index]
            # return True
        else:
            # If yes, add the key:value pair to it as the head, and set node.next to be the key:value pair that was
            # at the head.
            return False

        # If yes, add the key:value pair to it as the head, and set node.next to be the key:value pair that was at the
        # head.

    def get(self, key):
        pass

        # get
        # Arguments: key
        # Returns: Value associated with that key in the table

    def contains(self, key):
        pass

        # contains
        # Arguments: key
        # Returns: Boolean, indicating if the key exists in the table already.

    def keys(self):
        pass

        # keys
        # Returns: Collection of keys

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
