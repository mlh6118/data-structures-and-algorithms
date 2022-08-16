# Find Largest Value in Linked List - Blog

### Code
  ```
class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def ll_head_exists(self):
        if self.head is None:
            message = "Linked List head does not exist."
            raise TargetError(message)

    def find_largest_value_in_linked_list(self):
        current = self.head
        max_value = current
        current = current.next
        while current:
          if current > max_value:
            max_value = current
          current = current.next
        return max_value
  ```

### Sample Linked List
[8] -> [4] -> [42] -> [23] -> None

### Step-by-Step Explanation of Code
1. A class called LinkedList is defined which will hold the methods required.
2. The first method is the \_\_init__ method which has a parameter of self
   to pass things on to the other methods and a parameter of head which is
   needed to know where the linked list begins.
   1. The only statement within the \_\_init__ is `self.head = head` which
      assigns the value of head which was passed in to self.head allowing it
      to be used in other methods of the LinkedList class.  If no value for
      head is passed in, it is set to the default value which is "None".
      `self.head = [8]`
3. The next method is ll_head_exists which checks if the head of the linked
   list is known.  The only parameter for this method is "self".
   1. The first statement of this method is to check if the head is equal
      to "None".  If it is true, create a message assigning it the value
      "Linked List head does not exist."  Then raise a TargetError and pass
      the message in as an argument.
      `self.head is not None`  (Skip the rest of this method.)
4. Once the \_\_init__ has run and ll_head_exists does not raise an error,
   the last method, find_largest_value_in_linked_list would be executed.
   This method only has the parameter of "self".
   1. The first line assigns a variable called "current" to be self.head.
      `current = [8]`
   2. The next line assigns a variable called "max_value" to be current.
      `max_value = [8]`
   3. The following line assigns the variable "current" to now be the node
      that is in "current.next".
      `current = [4]`
   4. A while loop is entered if the condition of "current" exists.  Within
      the while loop, an if statement checks whether the variable "current"
      is greater than the variable "max_value".  If it is, then the variable
      "max_value" is reassigned to be "current".  After the if statement
      execution, "current" is reassigned to the node that is in "current.
      next".  The while loop repeats until "current" is "None".
      ```
      First iteration:
        current is True
        [4] > [8] (false - skip the "then" statement)
        current = [42]

      Second iteration:
        current is True
        [42] > [8] (true)
          max_value = [42]
        current = [23]

      Third iteration:
        current is True
        [23] > [42] (false - skip the "then" statement)
        current = None

      Fourth iteration:
      current is False (Break out of the loop.)
      ```
   5. The final line of the method returns the variable "max_value" to the
      point that called the method.
      `return max_value = [42]`
