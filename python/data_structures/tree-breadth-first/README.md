### Challenge Summary
Write a method that takes in a binary tree and returns a list of values in a
breadth-first order.

### Whiteboard Process
![breadth-first whiteboard](assets/breadth_first_whiteboard.jpg)

### Approach & Efficiency
The approach that was taken was to copy the invalid_operation_error.py,
queue.py, and trees.py files from previous projects into this project.  Then,
using a test driven development (TDD), write the code that would be needed.

Big O:
Space: O(n) because we are creating a new data structure in the form of a
queue which scales as we add more nodes.
Time: O(w) because we are looking at each level the tree at one time.

### API
__breadth_first__: takes in a tree and returns a list of values.

##### Worked with: Jae Loney, Brendon Hampton, Brian Tarte, Pedro Perez, Joey Marianer
