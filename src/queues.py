"""
Queue Classes

This module contains implementations of various queue types, including a generic Queue, LinearQueue,
IsaacsLinearQueue, and CircularQueue.

Author: Viren070 on GitHub
"""

from typing import Union

class Queue:
    """
    A generic queue class.

    Attributes:
    - type (str): The type of the queue.
    - max_size (int): The maximum capacity of the queue.
    - queue (list): The list representing the queue.
    - front (int): The index pointing to the front of the queue.
    - rear (int): The index pointing to the back of the queue.

    Methods:
    - __init__(self, max_size: int): Initializes a new Queue with the specified maximum size.
    - display_queue(self): Displays the current status of the queue.
    - size(self) -> bool: Returns the current size of the queue
    - is_full(self) -> bool: Checks if the queue is full.
    - is_empty(self) -> bool: Checks if the queue is empty.
    """
    def __init__(self, max_size):
        self.type = None
        self._max_size = max_size
        self._queue = [None]*max_size # initialise array with size of max_size
        self._front = 0
        self._rear = -1

    def display_queue(self):
        '''Display the queue status'''
        print(f"\nQueue Type: {self.type}\nQueue Array: {self._queue}\nFront Index: {self._front}\nRear Index: {self._rear}\nItem at front: {self.peek()}\nCurrent Queue Size: {self.size()}\nIs Full: {self.is_full()}\nIs Empty: {self.is_empty()}\n")

    def is_full(self) -> bool:
        ''' Return whether the queue is full or not'''
        return self._rear + 1 == self._max_size

    def is_empty(self) -> bool:
        '''Return True if queue is empty and False if not'''
        return self._front > self._rear

    def peek(self) -> str:
        '''Return the item at the front of the queue without removing it, or None if queue is empty'''
        return None if self.is_empty() else self._queue[self._front]

    def size(self) -> int:
        """Return the number of items currently in the queue"""
        return 0 if self.is_empty() else (self._rear - self._front ) + 1


class LinearQueue(Queue):
    """
    A simple implementation of a Linear Queue.

    Attributes:
    - type (str): The type of the queue, set to "Better Linear".
    - max_size (int): The maximum capacity of the queue.
    - queue (list): The list representing the linear queue.
    - front (int): The index pointing to the front of the queue.

    Methods:
    - __init__(self, max_size: int): Initializes a new LinearQueue with the specified maximum size.
    - is_empty(self) -> bool: Checks if the queue is empty.
    - is_full(self) -> bool: Checks if the queue is full.
    - size(self) -> bool: Returns the current size of the queue
    - peek(self): Returns the item at the front of the queue, or None if empty
    - enqueue(self, item): Adds an item to the rear of the queue.
    - dequeue(self): Removes and returns the item from the front of the queue.

    Note:
    This implementation follows the principles of a linear queue, where elements are added at the rear
    and removed from the front. When the queue is full, enqueue operations will be rejected.
    Dequeue operations shift all remaining elements to the left to maintain order.
    """
    def  __init__(self, max_size):
        super().__init__(max_size)
        self.type = "Linear"

    def enqueue(self, item_to_add) -> bool:
        '''Add an item to the queue'''
        if self.is_full():
            return False
        self._rear += 1
        self._queue[self._rear] = item_to_add
        return True

    def dequeue(self):
        '''Remove an item from the front of the queue and shift all items left'''
        if self.is_empty():
            return None

        dequeued_item = self._queue[self._front]
        self._front += 1
        if self._front != 0:
            for _ in range(self._front): # shift each item until the front index is 0
                self._queue[:] = self._queue[1:] + [None] # add None to end of list after shifting each item to the left.
            self._rear = self._rear - self._front # new rear would be the number of times shifted subtracted from old rear.
            self._front = 0
        return dequeued_item

class IsaacsLinearQueue(LinearQueue):
    """
    A simplified implementation of a Linear Queue, using Isacc Computer Science examples. Read the note for why this is incorrect.

    Attributes:
    - type (str): The type of the queue, set to "Linear".
    - max_size (int): The maximum capacity of the queue.
    - queue (list): The list representing the linear queue.
    - front (int): The index pointing to the front of the queue.
    - rear (int): The index pointing to the back of the queue

    Methods:
    - __init__(self, max_size: int): Initializes a new LinearQueue with the specified maximum size.
    - is_empty(self) -> bool: Checks if the queue is empty.
    - is_full(self) -> bool: Checks if the queue is full.
    - size(self) -> bool: Returns the current size of the queue
    - peek(self): Returns the item at the front of the queue or None if empty
    - enqueue(self, item): Adds an item to the rear of the queue.
    - dequeue(self): Removes and returns the item from the front of the queue.

    Note:
    This implementation follows **MOST** principles of a linear queue, where elements are added at the rear
    and removed from the front. When the queue is full, enqueue operations will be rejected.
    Dequeue operations **DO NOT** shift all remaining elements to the left. 
    """
    def  __init__(self, max_size):
        super().__init__(max_size)
        self.type = "Isaac's Linear"


    def dequeue(self) -> Union[str, None]:
        '''Remove an item from the front of the queue'''
        if self.is_empty():
            return None

        dequeued_item = self._queue[self._front]
        self._front += 1
        return dequeued_item

class CircularQueue(Queue):
    '''
    Create a circular queue that utilizes empty spaces at the front of the array caused by removing elements from the queue.

    Attributes:
    - type (str): The type of the queue, set to "Circular".
    - max_size (int): The maximum capacity of the circular queue.
    - queue (list): The list representing the circular queue.
    - rear (int): The index pointing to the last element in the queue.
    - front (int): The index pointing to the front element in the queue. Set to -1 when the queue is empty.

    Methods:
    - display_queue(self): Displays the current status of the circular queue.
    - is_full(self) -> bool: Returns True if the queue is full; otherwise, returns False.
    - is_empty(self) -> bool: Returns True if the queue is empty; otherwise, returns False.
    - size(self) -> bool: Returns the current size of the queue
    - peek(self): Returns the item at the front of the queue or None if empty
    - enqueue(self, item_to_add) -> bool: Adds an item to the end of the circular queue. Returns True on success, False if the queue is full.
    - dequeue(self): Removes and returns an item from the circular queue. Returns None if the queue is empty.

    Note:
    This implementation takes advantage of circular indexing to efficiently utilize the available space in the array.
    When the queue is full, further enqueue operations are rejected.
    Dequeue operations update the front and rear pointers, and if the queue becomes empty, these pointers are reset to -1.
    '''
    def __init__(self, max_size):
        super().__init__(max_size)
        self.type = "Circular"
        self._rear = -1
        self._front = -1

    def is_full(self):
        return (self._rear + 1) % self._max_size == self._front

    def is_empty(self):
        return self._front == -1

    def enqueue(self, item_to_add):
        '''Add an item to the end of the queue'''
        if self.is_full():
            return False
        self._rear = (self._rear + 1) % self._max_size
        self._queue[self._rear] = item_to_add
        self._front = 0 if self._front == -1 else self._front
        return True

    def dequeue(self):
        '''Remove an item from the queue'''
        if self.is_empty():
            return None
        dequeued_item = self._queue[self._front]
        if self._front == self._rear:
            self._front = -1
            self._rear = -1
        else:
            self._front = (self._front+1) % self._max_size
        return dequeued_item

    def size(self) -> int:
        if self.is_empty():
            return 0
        if self.is_full():
            return self._max_size
        return ((self._rear - self._front) + 1 ) % self._max_size


