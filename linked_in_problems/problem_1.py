"""This problem was asked by LinkedIn.

Determine whether a tree is a valid binary search tree.

A binary search tree is a tree with two children, left and right, and satisfies
the constraint that the key in the left child must be less than or 
equal to the root and the key in the right child must be greater than or equal to the root."""

class Node:

    def __init__(self, data=None):
        """
        Initialize data.

        Args:
            self: (todo): write your description
            data: (todo): write your description
        """
        self.data = data
        self.right = None
        self.left = None


class BinaryTree:

    def __init__(self):
        """
        Initialize the root node.

        Args:
            self: (todo): write your description
        """
        self.root = None

    def insert(self, data):
        """
        Insert data to root.

        Args:
            self: (todo): write your description
            data: (dict): write your description
        """
        node = Node(data)
        if not self.root:
            self.root = node
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        """
        Insert node at the tree.

        Args:
            self: (todo): write your description
            data: (todo): write your description
            node: (todo): write your description
        """
        if data < node.data:
            if node.left:
                self.insert_node(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right:
                self.insert_node(data, node.right)
            else:
                node.right = Node(data)

    def is_valid(self):
        """
        Return true if the node is valid.

        Args:
            self: (todo): write your description
        """
        return valid_node(self.root)

    def valid_node(self, node):
        """
        Validate node is a valid.

        Args:
            self: (todo): write your description
            node: (todo): write your description
        """
        if node:
            if node.left:
                if node.left.data > node.data :
                    return False
                else :
                    return self.valid_node(node.left)
            if node.right:
                if node.right.data <= node.data:
                    return False
                else :
                    return self.valid_node(node.left)
        else:
            return True
