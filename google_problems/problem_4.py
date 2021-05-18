"""This problem was asked by Google.
A unival tree (which stands for "universal value") is a tree where all nodes
under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
/\   / \
0 1  1   0
        / \
       1   0
"""

# FRIST WE NEED TO EMPLEMENT A TREE

class Tree:
   def __init__(self, data):
      self.data = data
      self.right = None
      self.left = None
      self.root = None

   def add_child(self, data):
      if self.right and data > self.right.data:
         if self.left is None:
            new_tree = Tree(data)
            new_tree.root = self.left
            self.left = new_tree
            return self.left
         self.left.add_child(data)

      if self.right is None:
         new_tree = Tree(data)
         new_tree.root = self.right
         self.right = new_tree
         return self.right
      self.right.add_child(data)
      
   def count_sub_trees(self):
      right_node = self.right is None
      left_node  = self.left is None
      if self.root is None :
         return 0
      if right_node and left_node:
         return 1
      if not right_node and not left_node: 
         root = self.root
         parents = 0
         while root.root is not None:
            parents += 1
         return  self.right.count_sub_trees()  + self.left.count_sub_tree() 




def emplement_tree():
   tree = Tree(0)
   tree.add_child(0)
   tree.add_child(1)
   tree.add_child(0)
   tree.add_child(1)
   tree.add_child(1)
   tree.add_child(1)
   print(tree.count_sub_trees())

if __name__ == "__main__":
   emplement_tree()