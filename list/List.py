from list.Node import Node


class List:
    """Represent a linear collection of nodes."""

    def __init__(self):
        self.__head: Node = None
        self.__tail: Node = None
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

    def __first_entry(self, node):
        self.head = node
        self.tail = node

        self.head.previous = self.tail
        self.tail.next = self.head
        self.len += 1

        return True

    def __insert_at_beginning(self, value):
        new_node = Node(value)

        if self.len == 0:
            return self.__first_entry(new_node)

        new_node.next = self.head
        self.head.previous = new_node
        self.head = new_node

        self.head.previous = self.tail
        self.tail.next = self.head
        self.len += 1
        return True

    def __remove_at_beginning(self):
        to_remove = self.head

        self.head = self.head.next
        self.tail.next = self.head
        self.head.previous = self.tail

        self.len -= 1

        to_remove.next = None
        to_remove.previous = None

        return to_remove

    def __insert_at_end(self, value):
        new_node = Node(value)

        if self.len == 0:
            return self.__first_entry(new_node)

        self.tail.next = new_node
        new_node.previous = self.tail
        self.tail = new_node
        self.head.previous = self.tail
        self.tail.next = self.head

        self.len += 1

        return True

    def __remove_at_end(self):
        to_remove = self.tail

        self.tail = self.tail.previous
        self.head.previous = self.tail
        self.tail.next = self.head

        self.len -= 1

        to_remove.next = None
        to_remove.previous = None

        return to_remove

    def prepend(self, value):
        return self.__insert_at_beginning(value)

    def push(self, value):
        return self.__insert_at_end(value)

    def pop(self, pos=None):

        if not pos:
            return self.__remove_at_end()
        elif pos == 0:
            return self.__remove_at_beginning()

    @staticmethod
    def split(string, sep=""):
        """Turn a string into a linked list by a separator, just like the built-in string function "split"
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
