class Node:
    def __init__(self, data):
        # Initialize a node with data and a pointer to the next node
        self.data = data
        self.pointer = None

class LinkedList:
    def __init__(self):
        # Initialize an empty linked list with no head
        self.head = None

    def get_list(self):
        """Traverse through nodes and create a list of data"""
        node = self.head
        result_list = []
        while node is not None:
            result_list.append(node.data)
            node = node.pointer
        return result_list

    def add_node_in_order(self, data):
        """Add a node with data to the linked list in ascending order"""
        new_node = Node(data)

        node = self.head
        if node is None:
            # If the list is empty, make the new node the head
            self.head = new_node
        elif new_node.data < node.data:
            # If the new node has smaller data, insert it at the beginning
            new_node.pointer = self.head
            self.head = new_node
        else:
            # Find the correct position to insert the new node
            while node.pointer is not None and node.pointer.data < new_node.data:
                node = node.pointer
            new_node.pointer = node.pointer
            node.pointer = new_node

    def add_node_at_front(self, data):
        """Add a node with data at the front of the linked list."""
        # Create a new node with the provided data
        new_node = Node(data)

        # Set the pointer of the new node to None
        new_node.pointer = None

        if self.head is not None:
            # If the linked list is not empty, set the pointer of the new node to the current head
            new_node.pointer = self.head

        # Set the head of the linked list to the new node, making it the new head
        self.head = new_node

    def delete(self, data):
        """Delete a node with specific data from the linked list"""
        node = self.head
        if node.data == data:
            # If the node to delete is at the front, change the head pointer
            self.head = node.pointer
            return True

        while True:
            # Iterate through nodes and delete the node with the specified data
            if node.pointer is None:
                # If the end of the list is reached and the data is not found, return False
                return False

            if node.pointer.data != data:
                # If the next node does not contain the data, continue iterating
                node = node.pointer
                continue

            # Break out of the loop if the data is found
            break

        # Adjust pointers to skip the node to be deleted
        node.pointer = node.pointer.pointer
        return True
