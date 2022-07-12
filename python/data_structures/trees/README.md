## Trees
Trees are non-linear data structures that can be more efficient to search
than something like a stack or a queue.

## Challenge
For this challenge, three classes were to be created: Node, BinaryTree, and
BinarySearchTree.  Within the BinaryTree and BinarySearchTree classes,
multiple methods were to be implemented.  These are described in the API
section below.

## Whiteboard Process
N/A

## Approach & Efficiency
The approach taken with this challenge was to use Test Driven Development and
run each test individually to see if it passed or failed.  If it failed,
then the error was resolved and tested again.  This process was repeated
until all tests passed.

### Big O:
__Binary Trees__
Time: O(n) because this is a binary tree which may need to be traversed
completely.
Space: O(n) because the list of values is creating a new data structure.

__Binary Search Trees__
Time: O(h) because the tree is cut in half each time a node on a given level
is checked.
Space: O(n) because the entire tree may need to be added to the stack.

## API
### Class Node:
__\_\_init____: Create a node with a value, a left, and a right.
__\_\_str____: Returns the value of the node.

### Class BinaryTree:
__pre_order__: Walks through a tree root, then left, then right and returns
a list of all values in the tree.
__in_order__: Walks through a tree left, then root, then right and returns
a list of all values in the tree.
__post_order__: Walks through a tree left, then right, then root and returns
a list of all values in the tree.
__find_maximum_value__: Returns the maximum value found in a binary tree.

### Class BinarySearchTree:
__add__: Walks through a binary search tree until it finds the correct
location to add the new node.
__contains__: Walks through a binary search tree until it finds the value
being searched for or it reaches the end of the tree and returns a boolean.
