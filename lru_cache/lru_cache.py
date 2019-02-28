
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
    # If key doesn't exist return None and do nothing with doubly linked list.

    # If key does exist, fetch Node
    pass

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
    pass