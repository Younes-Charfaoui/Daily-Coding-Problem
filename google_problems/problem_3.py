"""This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list. Instead of each
node holding next and prev fields, it holds a field named both, which is an XOR of
the next node and the previous  node. Implement an XOR linked list;
it has an add(element) which adds the element to the end, and a get(index) which
returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have
access to get_pointer and dereference_pointer functions that converts between
nodes and memory addresses."""


# Creating a class for the main linked list
class XorLinked(object):

    def __init__(self):
        """
        Initialize the object.

        Args:
            self: (todo): write your description
        """
        self.length = 0
        self.head = None

    def add(self, element):
        """
        Add an element to this node.

        Args:
            self: (todo): write your description
            element: (todo): write your description
        """
        if self.length == 0:
            nod = Node(element,0)
            self.head = element



def get_pointer(node):
    """
    Return the pointer of a node.

    Args:
        node: (todo): write your description
    """
    return 15

def dereference_pointer(pointer):
    """
    Dereference a pointer pointer.

    Args:
        pointer: (int): write your description
    """
    return Node(12,2)

# class of structure of node.
class Node(object):

    def __init__(self, value, xor):
        """
        Initialize the pointer.

        Args:
            self: (todo): write your description
            value: (todo): write your description
            xor: (todo): write your description
        """
        self.value = value
        self.xor_pointer = xor


