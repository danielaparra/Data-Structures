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
    pass

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
    pass

  def move_to_front(self, node):
    pass

  def move_to_end(self, node):
    pass

  def delete(self, node):
    pass
    
  def get_max(self):
    pass
