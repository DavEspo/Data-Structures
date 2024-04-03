# Class for the Node
class Node:
    # Constructor defining Node
    def __init__(self, data):
        self.data = data
        self.next = None

# Class for the LinkedList
class LinkedList:
    # Constructor defining LinkedList
    def __init__(self):
        self.head = None

    # Function to append an element to the LinkedList
    def InsertAtEnd(self, data):
        # Defines the new Node
        new_node = Node(data)

        # Test case where there is nothing in the LinkedList
        if self.head is None:
            self.head = new_node
            return

        # Sets the current Node variable to the 1st item in the Linked List
        curr_node = self.head

        # Shifts the node to the last position
        while curr_node.next:
            curr_node = curr_node.next

        # Appends the element
        curr_node.next = new_node

    # Function to print the LinkedList
    def printllist(self):
        # Sets the current Node variable to the 1st item in the Linked List
        curr_node = self.head

        # Prints each Node
        while (curr_node != None):
            print(curr_node.data, end = " ")
            curr_node = curr_node.next

    # Function to use the DummyNode to delete the 2nd Node from the end of the LinkedList
    def DummyNode(self, data):
        Dummy = Node(None)
        Head = self.head
        Dummy.next = Head
        Slow = Dummy
        Fast = Slow.next
        counter = 0

        # Test case where LinkedList is less than 2 Nodes
        if not Head or not Head.next or not Head.next.next:
            Fast.next == None
            return "Linked list too short"

        # Shifts the Fast pointer 2 spots
        while (counter < 2):
            Fast = Fast.next
            counter += 1

        # Shifts the Fast and Slow pointers at the same time until the end of the LinkedList
        while (Fast != None):
            Fast = Fast.next
            Slow = Slow.next

        # Removes the 2nd element from the end of the LinkedList
        Slow.next = Slow.next.next

# Creates a LinkedList
llist = LinkedList()

# Appends each number for each instruction
llist.InsertAtEnd(50)
llist.InsertAtEnd(11)
llist.InsertAtEnd(33)
llist.InsertAtEnd(21)
llist.InsertAtEnd(40)
llist.InsertAtEnd(71)

# Prints the LinkedList
print("Linked List: ", end = " ")
llist.printllist()
print()

# Calls the DummyNode Function
llist.DummyNode(llist.head.data)

# Prints the LinkedList after the DummyNode Function executed
print("Output: ", end = " ")
llist.printllist()
print()