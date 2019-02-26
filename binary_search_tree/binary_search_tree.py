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
     # If value added is greater than current node value, add to the right.
    if value > curr_node.value :
      # If current node's right child is None, set right child as new node with value.
      if not curr_node.right:
        curr_node.right = Node(value)
      # Otherwise call insert method again on current node's right child.
      else:
        self._insertRecursive(curr_node.right, value)
    # If value is less than or equal to current node value, add to the left.
    else:
      # If current node's left child is None, set left child as new node with value.
      if not curr_node.left:
        curr_node.left = Node(value)
      # Otherwise call insert method again on current node's left child.
      else:
        self._insertRecursive(curr_node.left, value)

  def insert(self, value):
    # If root value is None, set root value to given value.
    if not self.value:
      self.value = value
    # If value added is greater than root value, add to the right.
    elif value > self.value:
      self._insertRecursive(self, value)
    # If value is less than or equal to, add to the left.
    else:
      self._insertRecursive(self, value)

  def _containsRecursive(self, target, curr_node):
    # If search reaches a current node to None, it could not find target and return False.
    if curr_node is None:
      return False
    # If target equals current node value, return true.
    elif target == curr_node.value:
      return True
    # If target is greater than current node value, recurse through right child.
    elif target > curr_node.value:
      return self._containsRecursive(target, curr_node.right)
    # If target is less than current node value, recurse through left child.
    else:
      return self._containsRecursive(target, curr_node.left)

  def contains(self, target):
    # If target equals binary search tree root value, return true.
    if target == self.value:
      return True
    # If target is greater than binary search tree root value, recurse through root's right child.
    elif target > self.value:
      return self._containsRecursive(target, self.right)
    # If target is less than binary search tree root value, recurse through root's left child.
    else:
      return self._containsRecursive(target, self.left)

  def _get_max_recursively(self, curr_node):
    if not curr_node.right:
      return curr_node.value
    else:
      return self._get_max_recursively(curr_node.right)

  def get_max(self):
    if not self.right:
      return self.value
    else: 
      return self._get_max_recursively(self.right)
