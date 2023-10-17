# Python-Queues
Contains classes for Linear and Circular Queues with these methods:

- display_queue(self): Displays the current status of the circular queue.
- is_full(self) -> bool: Returns True if the queue is full; otherwise, returns False.
- is_empty(self) -> bool: Returns True if the queue is empty; otherwise, returns False.
- size(self) -> bool: Returns the current size of the queue
- peek(self): Returns the item at the front of the queue or None if empty
- enqueue(self, item_to_add) -> bool: Adds an item to the rear of the queue. Returns True on success, False if the queue is full.
- dequeue(self): Removes and returns an item from the circular queue. Returns None if the queue is empty.
- clear(self): Removes all items from the queue and reset pointer values.
