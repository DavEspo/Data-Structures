# Class to create a Node object
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
# Function to find the Max value on the left side of a particular Binary Tree
def bstMax(rootnode):
    if rootnode != None:
        while rootnode.right != None:
            rootnode = rootnode.right
        return rootnode.data
# Function to find the Mix value on the right side of a particular Binary Tree
def bstMin(rootnode):
    if rootnode != None:
        while rootnode.left != None:
            rootnode = rootnode.right
        return rootnode.data
# Function to check if the Binary Tree is a BST
def BST(ele):
    # Test case where there is nothing in the Binary Tree
    if ele is None:
        return "Binary Tree has nothing"
    # Variables that store the values of the Max of the left of the current Binary Tree and Min of the right of the current Binary Tree
    leftMax = bstMax(ele.left)
    rightMin = bstMin(ele.right)
    # Checks that there are actual values in the variables
    if ele != None and leftMax != None and rightMin != None:
        # Compares the values of the leftMax and rightMin with the parent Node to test for a valid BST
        if leftMax >= ele.data:
            return "Not a BST"
        if rightMin < ele.data:
            return "Not a BST"
    # Calls the BST function for every child Node and stores the result in the below variables
    left = BST(ele.left)
    right = BST(ele.right)
    # Checks the values of left and right to determine if the Binary Tree is a BST or not
    if left != "Not a BST" and right != "Not a BST":
        return "Is a BST"
    else:
        return "Not a BST"
# Creates the binary tree
root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)
# Calling the BST Function
print(BST(root))