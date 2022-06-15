@staticmethod
def zip_lists(a, b):
    """
    Args:
        a: A linked list.
        b: A second linked list.

    Note: Either a or b may be left empty.

    Returns:
        a: A zipped list
    """
    print("a: ", a)
    if a.head is None:
        return b
    if b.head is None:
        return a
    current_a = a.head
    current_b = b.head
    while current_a.next and current_b.next:
        temp_a = current_a.next
        temp_b = current_b.next
        current_a.next = current_b
        current_b.next = temp_a
        current_a = temp_a
        current_b = temp_b
        if current_a.next and current_b.next:
            temp_a = current_a.next
            temp_b = current_b.next
    if not current_a.next:
        current_a.next = current_b
    else:
        temp_a = current_a.next
        current_a.next = current_b
        current_b.next = temp_a
    return a
