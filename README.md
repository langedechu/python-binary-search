# python-binary-search

One dimensional binary search algorithm made using python.

## How it works?

The "binary search" algorithm is a searching method that is used to prevent the program to do lots and lots of steps before finding a certain value at a certain index.

First, it will take the length of an array, minus one, and store it as `high`. Same for the lowest value which will be stored as `low`.

The midpoint of these two values will be the important thing. If the value stored at the index `low + high // 2` is greater than the searched value, then the midpoint will become the new high.

If the value stored at the index `low + high // 2` is lower than the searched value, then the midpoint will become the new `low`.

And it goes on, and on, and on... Until it finally find the right value at the right index.
