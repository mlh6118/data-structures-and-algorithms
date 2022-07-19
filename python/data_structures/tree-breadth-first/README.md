### Challenge Summary
Conduct "FizzBuzz" on a k-ary tree while traversing through it to create a
new tree.  Set the values of each of the new nodes depending on the
corresponding node value in the source tree.

### Whiteboard Process
![k-ary trees - Frame 1.jpg](assets/k-ary%20trees%20-%20Frame%201.jpg)
![k-ary trees - Frame 2.jpg](assets/k-ary%20trees%20-%20Frame%202.jpg)

### Approach & Efficiency
The approach that was taken was to try to enqueue the active node, then
dequeue it and enqueue its children followed by changing the value to "fizz,
" "buzz," "fizzbuzz," or just a string containing the original number based
on how it was divisible, and finally putting the new value into a new node
into the new tree.

Big O:
* Space: O(2 * n) &rarr; O(n) because we are creating two new data structures
in the form of a queue which scales as we add more nodes and a new tree.
* Time: O(n<sup>2</sup>) because we are going through two nested loops, one for
the while and one for the inner for.

### API
__fizz_buzz_tree__: takes in a tree, performs fizzbuzz on it, and produces a
new tree with the results of fizzbuzz.

##### Worked with: Jae Loney, Pedro Perez, Sergii Otryshko
