"""This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s)
, which deserialize the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def add_child(self, data):
        if data.split('.')[-1] == 'left':
            if self.left:
                self.left.add_child(data)
                return 
            self.left = Node(val=data)
            return 
        if self.right:
            self.right.add_child(data)
            return 
        self.right = Node(val=data)
        return 
    def __str__(self):
        return self.val


def serialize(node):
    if node.left and node.right:
        return node.val +','  + serialize(node.right) + ','  + serialize(node.left) + ','
    if node.right:
        return node.val + ',' + serialize(node.right) + ','
    if node.left:
        return node.val + ',' + serialize(node.left) + ','
    return node.val

node = Node('root', Node('left', Node('left.left')), Node('right'))
print(serialize(node))

def deserialize(tree):
    tree = tree.split(',')
    node = Node(tree[0])
    for element in tree[1:]:
        if element != '':
            node.add_child(element)
    
    return node

assert deserialize(serialize(node)).left.left.val == 'left.left'
assert deserialize(serialize(node)).val == 'root'
