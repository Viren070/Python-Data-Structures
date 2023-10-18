from Structures.linked_lists import LinkedList


class Stack(LinkedList):

  def __init__(self):
    super().__init__()
    # Inheriting from LinkedList, a Stack initializes with an empty linked list.
    # The add_node_at_front function of LinkedList is equivalent to the push() method,
    # so we assign self.push to that method.
    self.push = self.add_node_at_front

  def is_empty(self):
    """Check if the stack is empty."""
    # The stack is empty if the head of the linked list is None.
    return self.head is None

  def pop(self):
    """Remove and return the top element of the stack (last added)."""
    if self.is_empty():
      # If the stack is empty, return False (indicating failure to pop).
      return False

    # Get the data from the current head (top of the stack).
    popped = self.head.data

    # Move the head pointer to the next node, effectively removing the top element.
    self.head = self.head.pointer

    # Return the popped element.
    return popped

  def peek(self):
    """Return the top element of the stack without removing it."""
    if self.is_empty():
      # If the stack is empty, return None.
      return None

    # Return the data from the current head (top of the stack).
    return self.head.data
