class Node:
  def __init__(self,value=None):
    self.value = value
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # If value added is greater than root value, add to the right.
    if value > self.value:
      new_node = Node(value)
      

  def contains(self, target):
    pass

  def get_max(self):
    pass
