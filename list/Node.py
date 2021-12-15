class Node:
    """
    Represent a node.
    ...
    Attributes
    ----------
    value : Any
        the value this node will hold.
    next : None | Any
        the next pointer of this node.
    previous : None | Any
        the previous pointer of this node.
    """

    def __init__(self, value):
        """
        Parameters
        ----------
        value : Any
            the value this node will hold.
        """
        self.value = value
        self.next = None
        self.previous = None
