"""This problem was asked by Google.

Invert a binary tree.

For example, given the following tree:

    a
   / \
  b   c
 / \\  /
d   e f
should become:

  a
 / \
 c  b
 \\  / \
  f e  d
"""

from collections import deque


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

    def invert_node(self):
        """
        Invert the node.

        Args:
            self: (todo): write your description
        """
        right = self.right
        self.right = self.left
        self.left = right


class BinaryTree:

    def __init__(self, root=None):
        """
        Initialize the root node.

        Args:
            self: (todo): write your description
            root: (str): write your description
        """
        self.root = root

    def invert(self):
        """
        Invert a node from the current node.

        Args:
            self: (todo): write your description
        """
        queue = deque()
        queue.append(self.root)
        while queue:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            node.invert_node()

    def breadth_traversal(self):
        """
        Returns a list of nodes in the dfs.

        Args:
            self: (todo): write your description
        """
        list_nodes = []
        queue = deque([self.root])
        while len(queue) > 0:
            node = queue.popleft()
            list_nodes.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return list_nodes


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f

tree = BinaryTree(a)
tree.invert()
print(tree.breadth_traversal())
