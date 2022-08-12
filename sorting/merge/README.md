# Blog Notes: Merge Sort

Pseudocode:
```
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
```

**Line by Line Explanation of Pseudocode**<br>
Accept an array (called "arr") in the MergeSort function as a parameter.

  &emsp;Declare a variable called "n" and assign it the length of the array.

  &emsp;Check if "n" is greater than 1.  If it is, do the following:<br>
    &emsp;&emsp;Declare a variable called "mid" and assign it to be "n"
  divided by 2.<br>
    &emsp;&emsp;Declare a variable called "left" and assign it the array
  from element 0 to element "mid".<br>
    &emsp;&emsp;Declare a variable called "right" and assign it the array
  from element "mid" to element "n".<br>
    &emsp;&emsp;Recursively call the MergeSort function and pass it the
  "left" to sort it.<br>
    &emsp;&emsp;Recursively call the MergeSort function and pass it the "right"
  to sort it.<br>
    &emsp;&emsp;Call the Merge function and pass it the arguments of "left",
  "right", and "arr".<br>

Accept the "left", "right", and "arr" as parameters in the Merge function.

  &emsp;Declare variables "i", "j", and "k" and set all three equal to 0.

  &emsp;Create a while loop that has the conditions of "i" smaller than the
  length of the "left" that was passed in and "j" is smaller than the length
  of the "right" that was passed in.  If both conditions are met, do the
  following:<br>
      &emsp;&emsp;Check if the value of element "i" in "left" is smaller
  than the element "j" in "right".  If it is, do the following:<br>
        &emsp;&emsp;&emsp;Assign the element of "i" in "left" to element "k"
  in "arr".<br>
        &emsp;&emsp;&emsp;Increase the value of "i" by 1.<br>
      &emsp;&emsp;If the value of element "i" in "left" is not smaller than
  the element "j" in "right", then do the following:<br>
        &emsp;&emsp;&emsp;Assign the element of "j" in "right" to element "k"
  in "arr".<br>
        &emsp;&emsp;&emsp;Increase the value of "j" by 1.<br>

  &emsp;&emsp;Increase the value of "k" by 1.<br>

  &emsp;Check if the value of "i" is equal to the length of "left".  If it
  is, do the following:<br>
    &emsp;&emsp;Change any leftover elements in "arr" to be the leftover
  values in "right".<br>
  &emsp;If the value of "i" is not equal to the length of "left", do the
  following:<br>
    &emsp;&emsp;Change any leftover elements in "arr" to be the leftover
  values in "left".<br>

**Sample Array**<br>
[8, 4, 23, 42, 16, 15]

**Step-Through**<br>
Enter the MergeSort function.<br>
  &emsp;Set "n" to be the length of the array that was passed in.<br>
  &emsp;`n = len(arr)`<br>

  &emsp;Check if "n" is greater than 1.<br>
  &emsp;`if n > 1:`<br>
    &emsp;&emsp;Declare variables and assign them values.<br>
    &emsp;&emsp;`mid = n/2`<br>
    &emsp;&emsp;`left = arr[8, 4, 23]`<br>
    &emsp;&emsp;`right = arr[42, 16, 15]`<br>

  &emsp;&emsp;Recursively call Mergesort and pass in "left".<br>
  &emsp;&emsp;`Mergesort(left)`<br>
      &emsp;&emsp;&emsp;First Iteration:<br>



  &emsp;&emsp;Recursively call Mergesort and pass in "right".<br>
  &emsp;&emsp;`Mergesort(right)`<br>
  &emsp;&emsp;Call the Merge function and pass in "left", "right", and "arr".
  <br>
  &emsp;&emsp;Merge(left, right, arr)<br>

