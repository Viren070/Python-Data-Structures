"""
Data Structures

This program allows users to interact with different types of data structures, including queues and linked lists.

Author: Viren070 on GitHub
"""
from typing import Union
import structures.queues as queues

from structures.linked_lists import LinkedList
from structures.stacks import Stack



def get_integer_within_limits(text: str,
                              lower_limit: Union[int, None] = None,
                              upper_limit: Union[int, None] = None
                              ) -> int:
    '''
    Obtain an integer input within optional limits.

    Parameters:
    - text (str): The prompt to display to the user.
    - lower_limit (int): The optional lower limit for the integer input.
    - upper_limit (int): The optional upper limit for the integer input.

    Returns:
    int: The validated integer input within the specified limits.
    '''
    integer = None
    while integer is None:
        try:
            integer = int(input(text))
            if lower_limit is not None and integer <= lower_limit:
                print(f"\nYou must enter a number greater than {lower_limit}")
                integer = None
            elif upper_limit is not None and integer >= upper_limit:
                print(f"\nYou must enter a number lower than {upper_limit}")
                integer = None
        except ValueError:
            print("\nPlease enter a valid integer")
    return integer

def initialise_queue():
    '''
    Initialize a queue based on user input for the maximum size and type of queue.

    Returns:
    LinearQueue or CircularQueue: The initialized queue based on user input.
    '''
    queue = None
    max_queue_size = get_integer_within_limits("\nEnter the maximum size of the queue: > ", 0)
    while queue is None:
        queue_option = input("\nWhat queue do you wish to use? \n1 - Linear Queue\n2 - Circular Queue\n: > ")
        match queue_option:
            case "1":
                queue = queues.LinearQueue(max_queue_size)
            case "2":
                queue = queues.CircularQueue(max_queue_size)
            case _:
                print("\nInvalid Choice.\n")
    return queue

def run_queue_menu(queue):
    '''
    Run the menu for interacting with the given queue.

    Parameters:
    - queue (LinearQueue or CircularQueue): The queue to interact with.
    '''
    while queue is not None:
        # menu for dequeuing and enqueuing
        queue.display_queue()
        user_choice = input("\nQueue Options:\n1 - Enqueue\n2 - Dequeue\n3 - Clear Queue\n4 - Back to Main Menu\n: > ")
        match user_choice:
            case "1":  # handle enqueue
                data = input("\nWhat do you want to enqueue? > ")
                if queue.enqueue(data):
                    print(f"\n{data} was added to the queue")
                else:
                    print(f"\nThe queue is full. {data} was not added to the queue")

            case "2":  # handle dequeue
                dequeue_result = queue.dequeue()
                if dequeue_result is None:
                    print("\nThere was nothing to dequeue; the queue is empty.")
                else:
                    print(f"\n{dequeue_result} was removed from the queue")
            case "3": # handle clear queue
                queue.clear()
            case "4":  # handle exit
                queue = None
            case _:  # handle other inputs
                print("\nInvalid choice")
        if user_choice != "4":
            input("\nPress enter to continue....")
def run_stack_menu(stack):
    while stack is not None:
        # menu for dequeuing and enqueuing

        stack_list = stack.get_list()
        print("=======================LIST====================")
        print(*stack_list, sep=" | ")
        print("===============================================")
        user_choice = input("\nStack Options:\n1 - Push item\n2 - Pop Item\n3 - Peek\n4 - Back to Main Menu\n: > ")
        match user_choice:
            case "1":
                data_to_add = input("\nEnter data to add for new node: ")
                stack.push(data_to_add)
            case "2":
                popped = stack.pop()
                if popped is not False:
                    print(f"\n{popped} was popped from the stack")
                else:
                    print("\nNothing to pop")
            case "3":
                peek_result = stack.peek()
                if peek_result:
                    print(f"\nItem at top of stock {peek_result}")
                else:
                    print("\nThe stack is empty, nothing at top of stack")
            case "4":  # handle exit
                stack = None
            case _:  # handle other inputs
                print("\nInvalid choice")

        _ = input("\nPress enter to continue....") if user_choice != "4" else None

def run_linked_list_menu(linked_list):

    while linked_list is not None:
        # menu for dequeuing and enqueuing
        linked_list_array = linked_list.get_list()
        print("=======================LIST====================")
        print(*linked_list_array, sep=" | ")
        print("===============================================")
        user_choice = input("\nLinked List Options:\n1 - Add Node at front\n2 - Add Node in ascending order\n3 - Delete Node\n4 - Back to Main Menu\n: > ")

        match user_choice:
            case "1":
                data_to_add = input("\nEnter data to add for new node: ")
                linked_list.add_node_at_front(data_to_add)
                print(f"\n{data_to_add} was added to the linked list")
            case "2":
                data_to_add = input("\nEnter data to add for new node in order: ")
                linked_list.add_node_in_order(data_to_add)
                print(f"\n{data_to_add} was added to the linked list in ascending order")
            case "3": # handle clear queue
                data_to_delete = input("\nEnter data to remove from list: ")
                result = linked_list.delete(data_to_delete)
                if result:
                    print(f"\n{data_to_delete} was removed from the linked list")
                else:
                    print(f"\n{data_to_delete} was not found in the linked list")
            case "4":  # handle exit
                linked_list = None
            case _:  # handle other inputs
                print("\nInvalid choice")

        if user_choice != "4":  # don't show this message if the user wants to exit
            input("\nPress enter to continue....")


if __name__ == "__main__":
    print("Welcome to the Python Data Structure Testing Environment. ")
    print("Please choose which data structure you would like to use.")
    while True:
        menu_choice = input("\nMain Menu:\n1 - Queues\n2 - Linked Lists\n3 - Stacks\n4 - Exit\n : > ")
        match menu_choice:
            case "1":
                run_queue_menu(initialise_queue())
            case "2":
                run_linked_list_menu(LinkedList())
            case "3":
                run_stack_menu(Stack())
            case "4":
                break
            case _:
                print("\nInvalid Choice")
