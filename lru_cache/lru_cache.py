
from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import ListNode

class LRUCache:
  def __init__(self, limit=10):
    # Initialize a doubly linked list to hold order of items in cache.
    self.dll = DoublyLinkedList()
    # A dictionary to fetch values based on keys in the dll.
    self.dictionary = dict()
    self.limit = limit

  """
  Retrieves the value associated with the given key. Also
  needs to move the key-value pair to the top of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache. 
  """
  def get(self, key):
    # Fetch node for given key.
    curr_node = self.dictionary.get(key)
    
    # If node does exist, move node to the front of doubly linked list.
    if curr_node:
      self.dll.move_to_front(curr_node)

    # Return current node.
    return curr_node

  """
  Adds the given key-value pair to the cache. The newly-
  added pair should be considered the most-recently used
  entry in the cache. If the cache is already at max capacity
  before this entry is added, then the oldest entry in the
  cache needs to be removed to make room. Additionally, in the
  case that the key already exists in the cache, we simply 
  want to overwrite the old value associated with the key with
  the newly-specified value. 
  """
  def set(self, key, value):
    # Check if key exists in dictionary.
    if key in self.dictionary:
      # If so, update value of node in dictionary.
      curr_node = self.dictionary[key]
      self.dictionary[key] = value
      # And move node to front of dll.
      self.dll.move_to_front(curr_node)
      return

    # Check it dll is at max capacity and it's assumed key is not in dictionary. 
    if len(self.dictionary) == self.limit:
    # If dll is at limit, remove lru-est node from dll and dictionary.
      self.dll.remove_from_tail()
      self.dictionary.pop(key)
    
    # Otherwise, add new node with key and value to dll and dictionary.
    # Bring node to the front of dll.
    new_node = self.dll.add_to_head(key, value)
    self.dictionary[key] = new_node
