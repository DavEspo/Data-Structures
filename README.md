# Data Structures
This repository contains the different Data Structures there are and demonstrates the Linear Data Structures and Non-Linear Data Structures. The Data Structures that were used in all the different files here were Lists, Dictionaries, Linked Lists, Queues, Stacks, Binary Trees, and Graphs. Each file uses a different Data Structure and the program does something accordingly with the Data Structure used.
## Linear Data Structures
Lists, Dictionaries, Linked Lists, Queues, and Stacks are the Linear Data Structures used here. Some of them are Built in and some are User Defined.
### Built in
The 2 Data Structures that are used here that are built into python are Lists and Dictionaries.
#### Dictionary.py
The Dictionary Data Structure is used in this file. There is a list of words given and the code groups the anagrams together. Anagrams are different words with the same letters and letter count. The code uses a character count and arranges there into the dictionary accordingly.
#### List.py
A list is generally the most used of all the Data Structures and this file makes use of it. This file determines whether 2 words are anagrams of each other or not. A list of length 26 is used and the first word increments each letter's corresponding position in the list by 1 and the second element decrements each letter's corresponding position in the list by 1. If the list is all 0's, then the words are anagrams of each other.
### User Defined
Linked Lists, Queues, and Stacks are user defined Linear Data Structures.
#### LinkedList.py
The LinkedList Data Structure is implemented in this file which handles an unordered list. Here, the nth node from the end of the Linked List is getting deleted and n=2. This is done by having a fast and slow pointer. A dummy node is also used to point to the head of the list. The slow pointer points to the dummy node and the fast one to the head of the Linked List. The fast pointer moves 2 places ahead and there will be a gap of 2 between the fast and slow pointers so that when the fast pointer reaches the end of the list, the 2nd to last node can be deleted.
#### Queue.py
The Queue Data Structure is used in this code.
#### Stack.py
This file makes use of the Stack Data Structure.
## Non-Linear Data Structures
Binary Trees and Graphs are examples of Non-Linear Data Structures and that are used here.
### Binary Tree
This folder contains 2 files which are ConstraintCheck.py and InOrderTraversal.py which make use of the Binary Tree Data Structure.
#### ConstraintCheck.py
This code does a check of constraints on the nodes to see if the Binary Tree is a Binary Search Tree. A Binary Search Tree is one in which the left child node is less than the root and the right child node is greater than the node and all child nodes regardless of the depth are supposed to be less on the left side and greater on the right side. So, this file outputs whether the Binary Tree is a Binary Search Tree or not.
#### InOrderTraversal.py
This code checks if the Binary Tree is a Binary Search Tree by doing In Order Traversal. This means that the nodes should be going in ascending order and if this is not the case somewhere along the Tree, then it isn't a Binary Search Tree. The output of this file returns whether it's a Binary Search Tree or not and if there is a Binary Search Tree, then it also returns the List of the Tree Traversal.
### Graph.py
This code makes use of the Graph Data Structure. It does a Depth First Search on a Graph iteratively and starts on Node 0. A stack is used for popping the nodes out after there is no deeper node. The output is a List of the DFS of the Graph. The Graph used in the code is visually showed in the image provided called Graph.png.
