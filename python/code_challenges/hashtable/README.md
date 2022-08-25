# Hashtables
Hashtables are a method of securely, but quickly storing data.  They are
comprised of a list of linked lists.  Each linked list entry contains
key:value pairs where the key has been encrypted using some sort of formula
that will always result in the same number (or index) where the data will be
stored.

## Challenge
The challenge was to write various methods to implement a hashtable.  See
the API section below for details of the various methods.

## Approach & Efficiency
#### Approach
The approach that was taken with this assignment was to do test driven
development (TDD).  While only three tests were provided, one of which was
just to check the class existed, a test was written prior to writing the
code for each of the required methods.  This allowed for checking small
steps along the way and then modifying the test to the next stage of the method.

#### Efficiency
Big O of Time: O(n) for all methods other than "set" because each contains
a single loop.  "Set" has an O(1) because the method access the existing
linked list directly and adds a new node to the head of it.

Big O of Space: O(n) because it is a list of linked lists.

## API
__set__: Hashes the key, places the key:value pair in the table, and handles
any collisions, as needed.

__get__: Converts the key to a hash, then searches the hash linked list for
the given key.  If the given key is found, the value is returned.

__contains__: Checks if the key already exists in the table and returns a
boolean.

__keys__: Goes through the entire table and returns a list of all the keys.

__hash__: Converts the key to a numeric value that will be consistent.  This
is based upon adding the ascii values of the characters in the key, then
multiplying by a prime number, and finally taking the modulo using the size
of the table.

##### Worked with Joey Marianer
