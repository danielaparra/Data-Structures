class Heap:
  def __init__(self):
    # Initialize storage array with None to start heap values at index 1.
    self.storage = [None]

  def insert(self, value):
    # Add new value to end of array.
    self.storage.append(value)
    # Get value's current index.
    curr_index = self.get_size()
    # Bubble up until it gets to the right position.
    self._bubble_up(curr_index)

  def delete(self):
    count = self.get_size()

    # If heap only holds only 1 value, pop it off and it's an empty array.
    if count == 1:
      self.storage.pop()
      return
    # If heap is greater than 1 element...
    elif count > 1:
      # Switch max(first) element with last element.
      self.storage[1], self.storage[count] = self.storage[count], self.storage[1]
      # Delete max value at the end of the array.
      self.storage.pop()
      # Sift down value to its new position in the heap.
      self._sift_down(1)

  def get_max(self):
    # Return none if heap is empty.
    if self.get_size() == 0:
      return None
    # Return first item that should be index 1.
    return self.storage[1]

  def get_size(self):
    # Return length of array minus the item in index 0.
    return len(self.storage) - 1

  def _bubble_up(self, index):
    # If value is at index 1, then it's at the top of the heap so do nothing more.
    if index <= 1:
      return
    
    # Get parent index of newly added value.
    parent_index = index // 2
    # If value at index is greater than at parent index, swap value and bubble up again.
    if self.storage[index] > self.storage[parent_index]:
      self.storage[index], self.storage[parent_index] = self.storage[parent_index], self.storage[index]
      self._bubble_up(parent_index)

  def _sift_down(self, index):
    count = self.get_size()

    # If index is already at the end of the array, do nothing more.
    if index == count:
      return
    # Get indexes for left and right children ``
    left_child = index * 2
    right_child = index * 2 + 1 
    # If heap has left and right child... 
    if count >= right_child:
      # Find out if right or left child is greater and save that index.
      greater_child_index = left_child if self.storage[left_child] > self.storage[right_child] else right_child
      # If child value is greater than the current index, swap values and sift down.
      if self.storage[greater_child_index] > self.storage[index]:
        self.storage[index], self.storage[greater_child_index] = self.storage[greater_child_index], self.storage[index]
        self._sift_down(greater_child_index)
    # If heap only has left child...
    elif count >= left_child:
      if self.storage[left_child] > self.storage[index]:
        self.storage[index], self.storage[left_child] = self.storage[left_child], self.storage[index]
        self._sift_down(left_child)
    else:
      return

