class Tree:    
    """A tree with BST functionality.
    """
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        """Initialize a tree with a root set to None.
        """
        self.root = None

    def add_root(self, root) -> None:
        """Add or update the root.
        """
        new_root = Tree.Node(root)
        if self.root is not None:
            # Update connections of old root's children
            new_root.left = self.root.left
            new_root.right = self.root.right
        self.root = new_root
    
    def contains_target(self, target) -> bool:
        def _contains_target(node, target):
            if node is not None:
                found = False
                found = _contains_target(node.left, target)
                if found:
                    return True
                found = _contains_target(node.right, target)
                if found:
                    return True
                found = target == node.data
                return found
            else:
                return False

        # Begin at the root.
        return _contains_target(self.root, target)

    def insert_data(self, data) -> None:
        def _insert_data(node, data):
            if node.data > data:
                if node.left is None:
                    new_node = Tree.Node(data)
                    node.left = new_node
                else:
                    # Dig deeper into the tree
                    _insert_data(node.left, data)
            elif node.data < data:
                if node.right is None:
                    new_node = Tree.Node(data)
                    node.right = new_node
                else:
                    # Dig deeper into the tree
                    _insert_data(node.right, data)
            else:
                # Generally, no duplicates allowed in BST
                return

        if self.root is None:
            self.add_root(data)
        else:
            _insert_data(self.root, data)


    ### UPDATED MACRO SOLUTION FOR ITERING OVER TREE ###
    def __iter__(self):
        def _rec_iter(node):
            if node.left is not None:
                yield from _rec_iter(node.left)
            if node is not None:
                yield node.data
            if node.right is not None:
                yield from _rec_iter(node.right)

        if self.root is None:
            yield "Nothing to iterate: tree is empty."
        else:
            yield from _rec_iter(self.root)

    ### UPDATED MACRO SOLUTION FOR DISPLAYING LENGTH ###
    def __len__(self) -> int:
        def _rec_len(node):
            number_of_elements = 0
            if node is not None:
                number_of_elements += 1
                number_of_elements += _rec_len(node.left)
                number_of_elements += _rec_len(node.right)
                return number_of_elements
            else:
                return 0

        # Begin at the root.
        return _rec_len(self.root)

def create_balanced_bst(list_of_items: list) -> Tree:
    """Create balanced bst by sorting the list and working on the list
    in halves.
    """
    def _create_balanced_bst(list_of_items, start_i, end_i, bst):
        if end_i < start_i:
            return
        elif end_i - start_i == 1:
            bst.insert_data(list_of_items[start_i])
            bst.insert_data(list_of_items[start_i+1])
            return
        elif end_i - start_i == 0:
            bst.insert_data(list_of_items[start_i])
            return
        else:
            middle = (end_i - start_i) // 2 + start_i
            bst.insert_data(list_of_items[middle])
            _create_balanced_bst(list_of_items, start_i,    middle - 1, bst)
            _create_balanced_bst(list_of_items, middle + 1, end_i,      bst)
            return

    # Create the tree to return and sort the given list.
    balanced_bst = Tree()
    list_of_items = sorted(list_of_items)
    
    middle = len(list_of_items) // 2
    try:
        balanced_bst.add_root(list_of_items[middle])
    # List was empty, so return empty bst.
    except IndexError:
        return balanced_bst

    _create_balanced_bst(list_of_items, 0,          middle - 1,             balanced_bst)
    _create_balanced_bst(list_of_items, middle + 1, len(list_of_items) - 1, balanced_bst)

    return balanced_bst