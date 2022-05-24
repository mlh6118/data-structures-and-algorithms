# Binary Search
Create a function which takes in two parameters: a sorted array and the
search key.  Return the index of the array's element that is equal to the
value of the search key, or -1 if the element is not in the array.

## Whiteboard Process
![BinarySearch whiteboard](Code%20Challenge%20Binary%20Search.png)

## Approach & Efficiency
The approach taken as to find the length of the existing array, then divide
by 2 and adjust by -1, if the array was an odd number of elements.  After
that, the search key was compared against the middle element of the array.
If the value was equal to the search key, the middle element was returned as
the index.  If the value was less than the search key, the array was saved
as a new array from index 0 to the index of the middle element previously
calculated.  If the value was greater than the search key, the array was
saved as a new array from the middle element as calculated to the end of the
array.  This process was repeated using a while loop with the condition that
the new array length was greater than 0.  Each time through the while loop,
the length of the array was verified to be greater than 1.  If it was equal
to 1, the function would return -1.

Big O: Space --> O(log N) and Time --> O(log N) because the program is a
binary search.

### Partner: Jacob Amsbury
