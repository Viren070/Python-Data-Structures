# Python-Queues
Comments and doc strings were written using ChatGPT.

Contains classes for these data structures:

- Queues 
- Linked Lists 
- Stacks 

### Queue Methods

- display_queue(self): Displays the current status of the circular queue.
- is_full(self) -> bool: Returns True if the queue is full; otherwise, returns False.
- is_empty(self) -> bool: Returns True if the queue is empty; otherwise, returns False.
- size(self) -> bool: Returns the current size of the queue
- peek(self): Returns the item at the front of the queue or None if empty
- enqueue(self, item_to_add) -> bool: Adds an item to the rear of the queue. Returns True on success, False if the queue is full.
- dequeue(self): Removes and returns an item from the circular queue. Returns None if the queue is empty.
- clear(self): Removes all items from the queue and reset pointer values.

### Linked List Methods

- get_list(self): Returns a list after traversing through the node
- add_node_in_order(self, data): Add a node to the linked list adhering to ascending order 
- add_node_at_front(self, data): Add a node with data to the front of the linked list 
- delete(self, data): Delete a node containing data given in parameter

### Stack Methods 

The stack data structure is implemented using a linked list.

- is_empty(self): Returns True if the stack is empty; otherwise, returns False
- pop(self): Remove and return the top element of the stack 
- peek(self): Returns the top element of the stack without removing it
