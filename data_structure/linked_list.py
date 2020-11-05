class Element(object):
    def __init__(self, value):
        """
        Initialize a new value.

        Args:
            self: (todo): write your description
            value: (todo): write your description
        """
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        """
        Initialize the head.

        Args:
            self: (todo): write your description
            head: (todo): write your description
        """
        self.head = head

    def append(self, new_element):
        """
        Append a new element to the end of the list.

        Args:
            self: (todo): write your description
            new_element: (todo): write your description
        """
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """
        Return the position of the current node.

        Args:
            self: (todo): write your description
            position: (todo): write your description
        """
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None

    def insert(self, new_element, position):
        """
        Inserts the current position at position.

        Args:
            self: (todo): write your description
            new_element: (todo): write your description
            position: (int): write your description
        """
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element

    def delete(self, value):
        """
        Remove the first item from the list.

        Args:
            self: (todo): write your description
            value: (str): write your description
        """
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next

    def print_list(self):
        """
        Prints a list.

        Args:
            self: (todo): write your description
        """
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result
