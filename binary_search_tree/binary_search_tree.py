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

  def _insertRecursive(self, curr_node, value):
     # If value added is greater than root value, add to the right.
    if curr_node.value > value:
      # If current node's right child is None, set right child as new node with value.
      if not curr_node.right:
        curr_node.right = Node(value)
      # Otherwise call insert method again on current node's right child.
      else:
        self._insertRecursive(curr_node.right, value)
    # If value is less than or equal to, add to the left.
    else:
      # If current node's left child is None, set left child as new node with value.
      if not curr_node.left:
        curr_node.left = Node(value)
      # Otherwise call insert method again on current node's left child.
      else:
        self._insertRecursive(curr_node.left, value)

  def insert(self, value):
    # If value added is greater than root value, add to the right.
    if value > self.value:
      self._insertRecursive(self, value)
    # If value is less than or equal to, add to the left.
    else:
      self._insertRecursive(self.left, value)

  def contains(self, target):
    pass

  def get_max(self):
    pass
