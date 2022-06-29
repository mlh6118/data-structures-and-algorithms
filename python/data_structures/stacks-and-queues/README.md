# Stacks and Queues
A stack is a data structure that consists of Nodes that are put in via FILO
(first in last out) and taken out via LIFO (last in first out).  A queue is
a data structure that also consists of Nodes, but they are put in via FIFO
(first in first out) and taken out via LILO (last in last out).

## Challenge
The challenge was to implement new classes called Stack and Queue.  The
Stack class was to have methods for push, pop, peek, and is_empty.  The
Queue class was to have methods for enqueue, dequeue, peek, and is_empty.
(See the API section for method descriptions.)

## Approach & Efficiency
The approach taken was to review each test that needed to pass individually,
then write a piece of code to pass that test.

Big O:
* Space: O(n) because we are added a new stack to simulate the queue.
* Time: O(n) because we are looping through a full stack to push a new node
  while simulating a queue.

## API
* Stack Methods:
  * __push__: Adds a new node to the top of the stack.
  * __pop__: Removes the top node of the stack and returns the value.
  * __peek__: Returns the value of the top node of the stack.
  * __is_empty__: Checks if the stack is empty and returns a boolean.
* Queue Methods:
  * __enqueue__: Adds a new node to the rear of the queue.
  * __dequeue__: Removes the front node of the queue and returns the value.
  * __peek__: Returns the value of the front node of the queue.
  * __is_empty__: Checks if the queue is empty and returns a boolean.
* PseudoQueue Methods:
  * __enqueue__: Pushes a new node to the top of the stack.
  * __dequeue__: Pops the top of the stack.

## Whiteboard Process
N/A

##### Worked with Sergii Otryshko
