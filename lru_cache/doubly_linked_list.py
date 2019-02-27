"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node

  def add_to_head(self, value):
    # Check if doubly linked list's head and tail are none.
    if not self.head:
      # Create new node and set as head and tail.
      new_node = ListNode(value)
      self.head = new_node
      self.tail = new_node
    else:
      # If it has an existing tail, insert new node before it.
      self.head.insert_before(value)
      # Reassign head to newly inserted node.
      self.head = self.head.prev

  def remove_from_head(self):
    # If linked list is empty return None.
    if not self.head:
      return None
    # If only one element in the linked list (e.g. self.head.next == None).
    elif not self.head.next:
      # Grab a second reference to our current head element 
      head = self.head
      # Set head and tail to None to represent an empty linked list.
      self.head = None
      self.tail = None
      # Return value of the old head element.
      return head.value
    # Otherwise more than one element in doubly linked list.
    else:
      # Grab a second reference to our current head element 
      head = self.head
      # Remove head element from linked list and rearranges pointers for next node.
      self.head.delete()
      # Reassign head to next node of the previous head.
      self.head = head.next
      # Return value of the old head element.
      return head.value

  def add_to_tail(self, value):
    # Check if doubly linked list's head and tail are none.
    if not self.head:
      # Create new node and set as head and tail.
      new_node = ListNode(value)
      self.head = new_node
      self.tail = new_node
    else:
      # If it has an existing tail, set after current tail.
      self.tail.insert_after(value)
      # Reassign tail to the new node.
      self.tail = self.tail.next


  def remove_from_tail(self):
    # If linked list is empty return None.
    if not self.head:
      return None
    # If only one element in the linked list (e.g. self.head.next == None).
    elif not self.head.next:
      # Grab a second reference to our current tail element 
      tail = self.tail
      # Set head and tail to None to represent an empty linked list.
      self.head = None
      self.tail = None
      # Return value of the old tail element.
      return tail.value
    # Otherwise more than one element in doubly linked list.
    else:
      # Grab a second reference to our current tail element 
      tail = self.tail
      # Remove tail element from linked list and rearranges pointers for prev node.
      self.tail.delete()
      # Reassign tail pointer to prev node
      self.tail = tail.prev
      # Return value of old tail element.
      return tail.value

  def move_to_front(self, node):
    # Check if linked list has more than one element or else do nothing.
    if self.head.next:
      # Grab a second reference to the node in question.
      newHead = node
      # Delete node and rearranges pointers for its prev and next nodes in the linked list.
      node.delete()
      # Reassign new head's prev and next nodes.
      newHead.prev = None
      newHead.next = self.head
      # Reassign current head's previous node.
      self.head.prev = newHead
      # Reassign head to new head.
      self.head = newHead

  def move_to_end(self, node):
    # Check if linked list has more than one element or else do nothing.
    if self.head.next:
      # Grab a second reference to the node in question.
      newTail = node
      # Delete node and rearranges pointers for its prev and next nodes in the linked list.
      node.delete()
      # Reassign new tail's prev and next nodes.
      newTail.prev = self.tail
      newTail.next = None
      # Reassign current tail's next node.
      self.tail.next = newTail
      # Reassign tail to new tail
      self.tail = newTail

  def delete(self, node):
    # If only one node in linked list
    if not self.head.next:
      # Set head and tail to None to represent an empty linked list.
      self.head = None
      self.tail = None
    # If the node in question is the head.
    elif node is self.head:
      # Grab a second reference to the node's next node.
      nextNode = node.next
      # Delete the node.
      node.delete()
      # Reassign the head to the next node.
      self.head = nextNode
    # If the node in question is the tail.
    elif node is self.tail:
      # Grab a second reference to the node's prev node.
      prevNode = node.prev
      # Delete the node.
      node.delete()
      # Reassign the head to the next node.
      self.tail = prevNode
    # Otherwise just delete the node.
    else:
      node.delete()
    
  def get_max(self):
    # Set the current node to the head of the linked list and the max value to the head's value.
    currNode = self.head
    maxValue = self.head.value
    # Traverse linked list.
    while currNode:
      # If the current node's value is greater than the maxValue, update the maxValue.
      if currNode.value > maxValue:
        maxValue = currNode.value
      currNode = currNode.next
    # Return the max value after looking at all the nodes' values.
    return maxValue
