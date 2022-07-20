

class LinkedList:
    """Define a doubly linked list
    """
    class Node:
        def __init__(self, data) -> None:
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def add_tail(self, data) -> None:
        new_node = LinkedList.Node(data)
        if self.tail is None:
            self.tail = self.head = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_and_return_head(self):
        # Get the current head
        return_head = self.head
        # Update connections between head and second node
        self.head.next.prev = None
        self.head = self.head.next
        return return_head.data