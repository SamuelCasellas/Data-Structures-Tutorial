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