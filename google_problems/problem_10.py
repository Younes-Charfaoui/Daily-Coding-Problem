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
        self.locked_counter = 0 
    def is_locked(self):
        return self.is_locked

    def add_node(self, data: int, is_locked: bool):
        if self.data > data:
            if self.right is None:
                if is_locked:
                    self.locked_counter += 1
                self.right = BinaryTree(data, None, None, is_locked)
                self.right.parent = self
                return
            else:
                self.right.add_node(data, is_locked)
        else:
            if self.left is None:
                if is_locked:
                    self.locked_counter += 1
                self.left = BinaryTree(data, None, None, is_locked)
                self.left.parent = self
                return
            else:
               self.left.add_child(data, is_locked)

    def check(self):
        if self.is_locked:
            return False
        if self.parent:
            are_not_locked = self.parent.check()  
            if are_not_locked:
                return False
        return True

    def lock(self):
        if self.check(): 
            self.is_locked = True
            curr = self.parent
            while curr:
                self.locked_counter += 1
                curr = curr.parent
            return True
        return False

    def unlocked(self):
        are_locked = self.check()
        if are_locked: 
            self.is_locked = True
            while curr:
                self.locked_counter -= 1
                curr = curr.parent
            return True
        return False
        
