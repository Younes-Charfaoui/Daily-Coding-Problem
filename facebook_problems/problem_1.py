"""This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message,
count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded
as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example,
'001' is not allowed."""


# Solution of this problem is given using a Tree data structure

class Node(object):

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class Tree(object):

    def __init__(self, string):
        self.root = Node(["", 0])
        self.string = string

    # count the number of branches, this is the solution
    def possible_branches(self):
        pass

    # get possible child for a node
    def get_nodes(self, position):
        pass
