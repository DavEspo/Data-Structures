# Class to create a Node object
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
# Function to go through In Order Traversal
def IOT(Root, list):
    # Test case where there is nothing in the Binary Tree
    if Root is None:
        return "Binary Tree is empty"
    # Test case where there are elements in the Binary Tree
    if Root:
        # Goes through In Order Traversal recursively and adds everything to the list
        IOT(Root.left, list)
        list.append(Root.data)
        IOT(Root.right, list)
        # Returns the list
        return list
# Function to test for a valid BST
def BST(Array):
    # Loop that goes through all elements in the list
    for i in range(len(Array) - 1):
        # Case for where the left node and parent node are getting compared
        if i % 2 == 0:
            # Checks that the list goes in ascending order
            if Array[i + 1] > Array[i]:
                continue
            else:
                return "Not a BST"
        # Case for where the parent node and the right node are getting compared
        else:
            # Checks that the list goes in ascending order
            if Array[i + 1] >= Array[i]:
                continue
            else:
                return "Not a BST"
    # Returns that it is a BST if the program reaches this point
    print("Is a BST")
    return list
# Creates the Binary Tree
root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)
# Creates a list
list = []
# Calls the BST function with the result of the IOT function as the parameter
print(BST(IOT(root, list)))