from structures.linked_lists import LinkedList

class Stack(LinkedList):
    def __init__(self):
        super().__init__()
        self.push = self.add_node_at_front
        
    def is_empty(self):
        return self.head is None
    
    def pop(self):
        if self.is_empty():
            return False 
        
        popped = self.head.data
        self.head = self.head.pointer
        return popped 
    
    def peek(self):
        if self.is_empty():
            return None 
        return self.head.data
        