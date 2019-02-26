class Heap:
  def __init__(self):
    # Initialize storage array with None to start heap values at index 1.
    self.storage = [None]

  def insert(self, value):
    # Add new value to end of array.
    self.storage.append(value)
    # Get value's current index.
    curr_index = self.get_size() - 1
    # Bubble up until it gets to the right position.
    self._bubble_up(curr_index)

  def delete(self):
    pass

  def get_max(self):
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
    if self.storage[index] > self.storage[parent_index]:
      self.storage[index], self.storage[parent_index] = self.storage[parent_index], self.storage[index]
      self._bubble_up(parent_index)

  def _sift_down(self, index):
    pass
