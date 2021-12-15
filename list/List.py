from list.Node import Node


class List:
    """Represent a linear collection of nodes."""

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__length = 0

    # Getters
    @property
    def head(self):
        return self.__head

    @property
    def tail(self):
        return self.__tail

    @property
    def len(self):
        return self.__length

    # Setters
    @head.setter
    def head(self, new_head):
        self.__head = new_head

    @len.setter
    def len(self, new_length):
        self.__length = new_length

    @tail.setter
    def tail(self, new_tail):
        self.__tail = new_tail

    def __str__(self):
        ptr = self.head
        txt = ""
        for i in range(self.len):
            txt += f"{ptr.value}, "
            ptr = ptr.next
        txt = txt.strip(", ")
        if self.len:
            return f"[{txt}]"
        else:
            return "[]"

    def __iter__(self):
        ptr = self.head
        for i in range(self.len):
            yield ptr
            ptr = ptr.next

    def push(self, value):
        """Push a new node holding an element to this list.
        Parameters
        ----------
        value : Any
            the value to pass it to the new node to push to this list.
        Returns
        -------
        bool
            True if the new node got pushed successfully.
        """
        new_node = Node(value)
        if not self.len:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
            self.head.previous = self.tail
            self.len += 1
            return True
        ptr = self.head
        while ptr and ptr.next != self.head:
            ptr = ptr.next

        ptr.next = new_node
        self.tail = new_node
        self.tail.previous = ptr
        self.tail.next = self.head
        self.head.previous = self.tail
        self.len += 1
        return True

    def pop(self, pos=None):
        """Pop a node from this list and return it.
        Parameters
        ----------
        pos : int
            The position where the node to delete is
        Returns
        -------
        Node
            The popped node.
        bool
            False in case this list's empty
        """
        if not self.len:
            print("No nodes in this list.")
            return False
        if pos is None:
            to_delete = self.tail
            self.tail = self.tail.previous
            self.tail.next = self.head
            self.head.previous = self.tail
            to_delete.next = None
            to_delete.previous = None
            self.len -= 1
            """For some reason, when working with stacks or queues, and you are popping nodes, there's gonna be always a
            remaining node which is the head and tail, and if you access to the len prop you'd see its len is 0 but
            there's a remaining node. Been tryna debug it but couldn't get to a fix. That's why I implemented this
            method, to ensure the head and tail is None when no nodes in list. Pretty sure you are smarter than me and
            would get to a fix. Please let me know! """
            self.__clear()
            return to_delete
        if pos == 0:
            to_delete = self.head
            self.head = self.head.next
            self.head.previous = self.tail
            self.tail.next = self.head
            to_delete.next = None
            to_delete.previous = None
            self.len -= 1
            self.__clear()
            return to_delete

        ptr = self.head
        index = 0

        while ptr and index != pos:
            ptr = ptr.next
            index += 1
            if ptr == self.head and index != pos:
                return False
        to_delete = ptr
        if ptr.next == self.head:
            self.tail = ptr.previous
            self.tail.next = self.head
            self.head.previous = self.tail
            ptr.previous = None
            ptr.next = None
            to_delete.previous = None
            to_delete.next = None
            self.len -= 1
            self.__clear()
            return to_delete
        else:
            ptr.previous.next = ptr.next
            ptr.next.previous = ptr.previous
            ptr.next = None
            ptr.previous = None
            to_delete.previous = None
            to_delete.next = None
            self.len -= 1
            self.__clear()
            return to_delete

    def get_value_at(self, pos):
        """Get a value in a specified position. Perfect when it comes to traverse the entire list with a for loop
        instead of a while one.
        Parameters
        ----------
        pos : int
            the position where the node to get is.
        Returns
        -------
        Any
            the value the node in the position is holding.
        bool
           False if no nodes were found in this list and plus if we traverse the entire list and didn't find the node in the position.
        """
        if not self.len:
            print("No nodes in this list.")
            return False
        ptr = self.head
        index = 0
        while ptr:
            if index == pos:
                return ptr.value
            ptr = ptr.next
            index += 1
            if ptr == self.head and index != pos:
                return False
        return False

    def __clear(self):
        if not self.len:
            self.head = None
            self.tail = None
            return True
        return False


def split(string, sep=" "):
    """Turn a string into a linked list by a separator, just like built-in string function "split"
    Parameters
    ----------
    string : str
        The string to turn into linked list.
    sep : str, optional
        The seperator, by default " "
    Returns
    -------
    List
        a linked list containing the string splitted by the separator as nodes.
    """
    if not string:
        return False
    if sep not in string:
        return False
    splitted_list = List()
    txt = ""
    for char in string:
        if char == sep:
            splitted_list.push(txt)
            txt = ""
        else:
            txt += char
    if txt:
        splitted_list.push(txt)
    return splitted_list
