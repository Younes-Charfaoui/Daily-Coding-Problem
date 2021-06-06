"""This problem was asked by Google.
Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all of its descendants or ancestors are not locked.
Design a binary tree node class with the following methods:
•	is_locked, which returns whether the node is locked
•	lock, which attempts to lock the node. If it cannot be locked, then it should return false. Otherwise, it should lock it and return true.
•	unlock, which unlocks the node. If it cannot be unlocked, then it should return false. Otherwise, it should unlock it and return true.
You may augment the node to add parent pointers or any other property you would like. You may assume the class is used in a single-threaded program, so there is no need for actual locks or mutexes. Each method should run in O(h), where h is the height of the tree.
"""


class BinaryTree:
    def __init__(self, data, left, right, is_locked):
        self.data = data
        self.left = left
        self.right = right
        self.parent = None
        self.is_locked = is_locked

    def is_locked(self):
        return self.is_locked

    def add_node(self, data: int, is_locked: bool):
        if self.data > data:
            if self.right is None:
                self.right = BinaryTree(data, None, None, is_locked)
                self.right.parent = self
                return
            else:
                self.right.add_node(data, is_locked)
        else:
            if self.left is None:
                self.left = BinaryTree(data, None, None, is_locked)
                self.left.parent = self
                return
            else:
               self.left.add_child(data, is_locked)
              
    def lock(self):
        if self.is_locked:
            return False
        if self.parent:
            are_not_locked = self.parent.lock()  
            if not are_not_locked:
                return False
        if self.right:
            are_not_locked = self.right.lock()
            if are_not_locked:
                return False
        if self.left:
            are_not_locked = self.left.lock()
            if are_not_locked:
                return False
        return True
    
    def unlocked(self):
        if self.is_locked:
            return False
        if self.right.is_locked or self.left.is_locked:
            return False
        self.is_locked = True
        return True
