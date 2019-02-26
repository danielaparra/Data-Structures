class Heap:
  def __init__(self):
    # Initialize storage array as an empty array.
    self.storage = []

  def insert(self, value):
    # Add new value to end of array.
    self.storage.append(value)
    # Get value's current index.
    curr_index = self.get_size() - 1
    # Bubble up until it gets to the right position.
    self._bubble_up(curr_index)

  def delete(self):
    count = self.get_size()

    # If heap only holds only 1 value, pop it off and it's an empty array.
    if count == 1:
      return self.storage.pop()
    # If heap is greater than 1 element...
    elif count > 1:
      # Switch max(first) element with last element.
      self.storage[0], self.storage[count - 1] = self.storage[count - 1], self.storage[0]
      # Delete max value at the end of the array.
      maxValue = self.storage.pop()
      # Sift down value to its new position in the heap.
      self._sift_down(0)
      return maxValue

  def get_max(self):
    # Return none if heap is empty.
    if self.get_size() == 0:
      return None
    # Return first item that should be index 0.
    return self.storage[0]

  def get_size(self):
    # Return length of array.
    return len(self.storage)

  def _bubble_up(self, index):
    # If value is at index 0, then it's at the top of the heap so do nothing more.
    if index <= 0:
      return
    
    # Get parent index of newly added value.
    parent_index = (index - 1) // 2
    # If value at index is greater than at parent index, swap value and bubble up again.
    if self.storage[index] > self.storage[parent_index]:
      self.storage[index], self.storage[parent_index] = self.storage[parent_index], self.storage[index]
      self._bubble_up(parent_index)

  def _sift_down(self, index):
    count = self.get_size()

    # If index is already at the end of the array, do nothing more.
    if index == count - 1:
      return
    # Get indexes for left and right children ``
    left_child = index * 2 + 1
    right_child = index * 2 + 2 
    # If heap has left and right child... 
    if count - 1 >= right_child:
      # Find out if right or left child is greater and save that index.
      greater_child_index = left_child if self.storage[left_child] > self.storage[right_child] else right_child
      # If child value is greater than the current index, swap values and sift down.
      if self.storage[greater_child_index] > self.storage[index]:
        self.storage[index], self.storage[greater_child_index] = self.storage[greater_child_index], self.storage[index]
        self._sift_down(greater_child_index)
    # If heap only has left child...
    elif count - 1 >= left_child:
      if self.storage[left_child] > self.storage[index]:
        self.storage[index], self.storage[left_child] = self.storage[left_child], self.storage[index]
        self._sift_down(left_child)
    else:
      return

