# Find Largest Value in Binary Search Tree - Blog

### Code
```
class BinarySearchTree:

    def walk(root, node):

        if not root:
            return

        max_value = root.value

        if node.value < root.value:
            if root.left:
                walk(root.left, node)
            else:
                root.left = node
        else:
            if root.right:
                walk(root.right, node)
            else:
                root.right = node

    walk(root, node)
```

### Sample Binary Search Tree
          13
      7      20
    1  9    15  27

### Step-by-Step Explanation of Code
1. A class called BinarySearchTree is defined which will hold the methods
required.
2. The only method is called "walk" which takes in the parameters of root
   and node.  It checks if the root does not exist.  If it does not, it
   returns back to the method call.  If the root does exist, then the node
   is set up in a separate class that creates the root.value, root.left,
   and root.right assignments.  For our sample binary tree, the values are
   as follows:
  ```
  root.value = 13
  root.left = 7
  root.right = 20
  ```
  Additionally, the call-stack will now look like the following:
  ```
  ----
   7
  ----
   20
  ----
  ```
3.
