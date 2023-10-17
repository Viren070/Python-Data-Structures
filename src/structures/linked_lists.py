class Node:
    def __init__(self, data):
        self.data = data
        self.pointer = None 

class LinkedList:
    def __init__(self):
        self.head = None 
        
    def traverse_nodes(self):  # create a list by traversing through nodes then print that list 
        node = self.head
        list = []
        while node is not None:
            list.append(node.data)
            node = node.pointer
        print("=======================LIST====================")
        print(*list, sep=",")
        print("===============================================")
            
    def add_node_in_order(self, data):
        new_node = Node(data)
        
        node = self.head
        if node is None:
            self.head = new_node 
            
        elif new_node.data < node.data:
            new_node.pointer = self.head
            self.head = new_node 
        else:
            while (node.pointer is not None and node.pointer.data < new_node.data):
                node = node.pointer 
            new_node.pointer = node.pointer 
            node.pointer = new_node 
    
    def add_node_at_front(self, data):
        """add a node at the front of the linked list taking data as a parameter"""
        new_node = Node(data)
        new_node.pointer = None 
        if self.head is None:
            self.head = new_node
        else:
            new_node.pointer = self.head # change pointer of new new_node to the previous first item (head)
            self.head = new_node
            
    def delete(self, data):
        node = self.head
        if node.data == data:   # if item to delete is at front then change head pointer 
            self.head = node.pointer
            return True
       
        while True: # iterate through each node and compare data, if found then break out of loop.
            if node.pointer is None:
                return False 
            
            if node.pointer.data != data:
                node = node.pointer
                continue 
            break                
        node.pointer = node.pointer.pointer
        return True 
