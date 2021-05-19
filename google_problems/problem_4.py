"""This problem was asked by Google.
A unival tree (which stands for "universal value") is a tree where all nodes
under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

            0
           / \
          1   0
         /\   / \
        1  0 1   0
            / \
           1   1
"""

# FRIST WE NEED TO EMPLEMENT A TREE

class BSTNode:
   def __init__(self, data):
      self.data = data
      self.right = None
      self.left = None

   def add_child(self, data):
      if self.data > data:
         if self.right is None:
            self.right = BSTNode(data)
            return
         else:
            self.right.add_child(data)
      else:
         if self.left is None:
            self.left = BSTNode(data)
            return
         else:
            self.left.add_child(data)
      
   def count_sub_trees(self, k=0):
      right_node = self.right is None
      left_node  = self.left is None
      if right_node and left_node:
         return k
      if not right_node and left_node:
         return k + self.right.count_sub_trees(k) 
      if right_node or not left_node: 
         return k + self.left.count_sub_trees(k) 
      if not right_node and not left_node:    
         return self.left.count_sub_trees(k) + self.right.count_sub_trees(k) + k

   def nodes(self, arr=[]):
      if self.left:
         arr.append(self.data)
         self.left.nodes(arr)
      if self.right:
         arr.append(self.data)
         self.right.nodes(arr)
      arr = arr.append(self.data)
      return arr

      
      


def emplement_tree():
   tree = BSTNode(0)
   tree.add_child(0)
   tree.add_child(1)
   tree.add_child(0)
   tree.add_child(1)
   tree.add_child(1)
   tree.add_child(1)
   print(tree.nodes())

if __name__ == "__main__":
   emplement_tree()