# Stacks and Queues
A stack is a data structure that consists of Nodes that are put in via FILO
(first in last out) and taken out via LIFO (last in first out).  A queue is
a data structure that also consists of Nodes, but they are put in via FIFO
(first in first out) and taken out via LILO (last in last out).

## Challenge
The challenge was to implement two new classes.  The first called Stack which
would have methods to push, pop, peek, and check if the stack is empty.  The
second called Queue which would have methods to enqueue, dequeue, peek,
and check if the queue is empty.

## Approach & Efficiency
The approach taken was to review each test that needed to pass individually,
then write a piece of code to pass that test.

Big O:
* Space: O(1) because we are adding a single node at a time to the stack or
  queue.
* Time: O(1) because we are not looping through anything, we are accessing a
  single node that is already being pointed to.

## API
* Stack Methods:
  * __push__: Adds a new node to the top of the stack.
  * __pop__: Returns the value of the top node of the stack and removes the
    node.
  * __peek__: Returns the value of the top node of the stack without removal.
  * __is_empty__: Returns a boolean indicating if the stack is empty.
* Queue Methods:
  * __enqueue__: Adds a new node to the back of the queue.
  * __dequeue__: Returns the value of the front node of the queue and
    removes the node.
  * __peek__: Returns the value of the front node of the queue without removal.
  * __is_empty__: Returns a boolean indicating if the queue is empty.
