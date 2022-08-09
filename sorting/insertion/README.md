# Blog Notes: Insertion Sort

Pseudocode:
```
InsertionSort(int[] arr)

  FOR i = 1 to arr.length

    int j <-- i -1
    int temp <-- arr[i]

    WHILE j >= 0 AND temp < arr[j]
      arr[j + 1] <-- arr[j]
      j <-- j - 1

    arr[j + 1] <-- temp
```

**Line by Line Explanation of Pseudocode**<br>
Accept an array in the InsertionSort function as an argument.

  &emsp;Create a for loop that will start at i = 1 and continue looping until it
  reaches the total number of elements in the array.

  &emsp;Create an integer called j that will point to i minus 1.<br>
  &emsp;Create a variable called temp that will point to the element i of the array.

  &emsp;Create a while loop that has the conditions j greater than or equal to 0
  and the temp variable is smaller than the element of j of the array.<br>
    &emsp;&emsp;The element of j plus 1 of the array will point to element j of the
  array.<br>
    &emsp;&emsp;The value of j will point to the value of j minus 1.

  &emsp;The element of j plus 1 of the array will point to the temp variable.

**Sample Array**<br>
[8, 4, 23, 42, 16, 15]

**Step-Through**<br>
First iteration:<br>
We set the variables as<br>
i = 1, j = i - 1 = 0, and temp = arr[1] = 4.<br>
Then we take a look at the while loop conditions.<br>
j >= 0 (True) and temp = 4 < arr[j] = 8 (True)<br>
Since both conditions are true, we enter the while loop and set<br>
arr[j+1] = arr[j] = 8.<br>
We then decrement j by 1 and check the while conditions.<br>
j = j - 1 = 0 - 1 = -1<br>
j >= 0 (False)<br>
Since j is not greater than or equal to 0, we immediately break out of the
while loop and proceed to set<br>
arr[j + 1] = arr[1] = temp = 8<br>
Our sample array changes look like this:<br>
[8, 4, 23, 42, 16, 15] --> [4, 8, 23, 42, 16, 15]

Second iteration:<br>
We set the variables as<br>
i = 2, j = i - 1 = 1, and temp = arr[2] = 23.<br>
Then we take a look at the while loop conditions.<br>
j >= 0 (True) and temp = 23 < arr[j] = 8 (False)<br>
Since temp is not greater than arr[j], we immediately break out of the while
loop and proceed to set<br>
arr[j + 1] = arr[1] = temp = 23<br>
Our sample array does not appear to have changed on this iteration:<br>
[4, 8, 23, 42, 16, 15] --> [4, 8, 23, 42, 16, 15]

Third iteration:<br>
We set the variables as<br>
i = 3, j = i - 1 = 2, and temp = arr[3] = 42.<br>
Then we take a look at the while loop conditions.<br>
j >= 0 (True) and temp = 42 < arr[j] = 23 (False)<br>
Since temp is not greater than arr[j], we immediately break out of the while
loop and proceed to set<br>
arr[j + 1] = arr[1] = temp = 42<br>
Our sample array does not appear to have changed on this iteration:<br>
[4, 8, 23, 42, 16, 15] --> [4, 8, 23, 42, 16, 15]

Fourth iteration:<br>
We set the variables as<br>
i = 4, j = i - 1 = 3, and temp = arr[4] = 16.<br>
Then we take a look at the while loop conditions.<br>
j >= 0 (True) and temp = 16 < arr[j] = 42 (True)<br>
Since both conditions are true, we enter the while loop and set<br>
arr[j+1] = arr[j] = 16.<br>
We then decrement j by 1 and check the while conditions.<br>
j = j - 1 = 3 - 1 = 2<br>
Then we take a look at the current while loop conditions.<br>
j >= 0 (True) and temp = 16 < arr[j] = 23 (True)<br>
arr[j + 1] = arr[1] = temp = 16<br>
We then decrement j by 1 and check the while conditions.<br>
j = j - 1 = 2 - 1 = 1<br>
Then we take a look at the current while loop conditions.<br>
j >= 0 (True) and temp = 16 < arr[j] = 8 (False)<br>
Since temp is not greater than arr[j], we immediately break out of
the while loop and proceed to set<br>
arr[j + 1] = arr[2] = temp = 16<br>
Our sample array changes look like this:<br>
[4, 8, 23, 42, 16, 15] --> [4, 8, 16, 23, 42, 15]<br>

Fifth iteration:<br>
We set the variables as<br>
i = 5, j = i - 1 = 4, and temp = arr[5] = 15.<br>
Then we take a look at the while loop conditions.<br>
j >= 0 (True) and temp = 15 < arr[j] = 42 (True)  <br>
Since both conditions are true, we enter the while loop and set<br>
arr[j+1] = arr[j] = 15.<br>
We then decrement j by 1 and check the while conditions.<br>
j = j - 1 = 4 - 1 = 3<br>
Then we take a look at the current while loop conditions.<br>
j >= 0 (True) and temp = 15 < arr[j] = 23 (True)<br>
Since both conditions are true, we enter the while loop and set<br>
arr[j + 1] = arr[1] = temp = 15<br>
We then decrement j by 1 and check the while conditions.<br>
j = j - 1 = 3 - 1 = 2<br>
Then we take a look at the current while loop conditions.<br>
j >= 0 (True) and temp = 15 < arr[j] = 16 (True)<br>
Since both conditions are true, we enter the while loop and set<br>
arr[j + 1] = arr[1] = temp = 15<br>
We then decrement j by 1 and check the while conditions.<br>
j = j - 1 = 2 - 1 = 1<br>
Then we take a look at the current while loop conditions.<br>
j >= 0 (True) and temp = 15 < arr[j] = 8 (False)<br>
Since temp is not greater than arr[j], we immediately break out of
the while loop and proceed to set<br>
arr[j + 1] = arr[2] = temp = 15<br>
Our sample array changes look like this:<br>
[4, 8, 16, 23, 42, 15] --> [4, 8, 15, 16, 23, 42]

