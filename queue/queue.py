
from linked_list_py import LinkedList

class Queue:
  def __init__(self):
    self.size = 0
    self.storage = LinkedList()

  def enqueue(self, item):
    self.storage.add_to_tail(item)
  
  def dequeue(self):
    return self.storage.remove_head()

  def len(self):
    currNode = self.storage.head
    count = 0
    while currNode is not None:
      nextNode = currNode.get_next()
      count += 1
      currNode = nextNode
    
    return count