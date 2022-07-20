

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

    ### INCLUDED ADD HEAD METHOD ###
    def add_head(self, data) -> None:
        new_node = LinkedList.Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def remove_and_return_head(self):
        # Get the current head
        return_head = self.head
        # Update connections between head and second node
        self.head.next.prev = None
        self.head = self.head.next
        return return_head.data

    # ### INCLUDED RETURN TAIL METHOD ###
    # def remove_and_return_tail(self):
    #     # Get the current tail
    #     return_tail = self.tail
    #     # Update connections of tail and second to last node
    #     self.tail.prev.next = None
    #     self.tail = self.tail.prev
    #     return return_tail.data

    ### INCLUDED INSERT NEW DATA LOGIC ###
    def insert_data_ordered(self, data, index=None, replace_seq="") -> None:
        """Insert a new node in linked list so that the order of the data is preserved
        Assume that the data is in ascending order.
        index: if the node's data is a list and a specific data needs to be assessed.
        """
        # 4 outcomes:
        # 1. The data is smaller than the rest of the data (new head needed)
        # 2. Inserting to the middle of the linked list
        # 3. No data: Add a new node that both head and tail point to (the add_tail() method takes care of this)
        # 4. The data is larger than the rest of the data (new tail needed)
        # (Cases 3 and 4 can both be resolved with add_tail()!)

        
        # In case #2 of inserting a node in the middle, 5 Steps are needed
        # 1. Make the new node
        # 2. Point the new node's pointer to next node to the current node
        # 3. Point the new node's pointer to prev node to the current node's previous node
        # 4. Point the current node's pointer to prev to the new node
        # 5. Point the current node's previous node's pointer to next node to the new node

        save_data = data

        # For list parsing if requested.
        if index is not None:
            data = list(data)[index]

        curr_node = self.head
        while curr_node is not None:
            # For list parsing if requested.
            if index is not None:
                curr_node_data = list(curr_node.data)[index]
            try:
                curr_node_data = curr_node_data.replace(replace_seq, "")
                data = data.replace(replace_seq, "")
            # If the data is not a string
            except AttributeError:
                pass

            if curr_node_data > data:
                # Case #1
                if curr_node == self.head:
                    self.add_head(save_data)
                    return
                # Case #2: We are inserting in the middle. See the five steps as follows.
                else:
                    new_node = LinkedList.Node(save_data)
                    new_node.next = curr_node
                    new_node.prev = curr_node.prev
                    curr_node.prev.next = new_node
                    curr_node.prev = new_node
                    return

            # Go to the next node
            curr_node = curr_node.next

        # Case #3 and #4: 
        self.add_tail(save_data)

    ### ADDED __ITER__ MACRO AS REQUIRED BY PREVIOUS METHOD ###
    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield current_node.data
            current_node = current_node.next
