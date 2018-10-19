"""This problem was asked by LinkedIn.

Determine whether a tree is a valid binary search tree.

A binary search tree is a tree with two children, left and right, and satisfies
the constraint that the key in the left child must be less than or 
equal to the root and the key in the right child must be greater than or equal to the root."""

class Node:

    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None


class BinaryTree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        node = Node(data)
        if not self.root:
            self.root = node
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
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
