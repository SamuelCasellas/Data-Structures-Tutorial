class LinkedList:

    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self) -> None:
        self.head = None
        self.tail = None