
Certified Entry-Level Python Programmer Certification


CHAPTER 14.6
Using `range`

Sometimes we want to iterate a set number of times, but we don't necessarily have a collection to work with. An easy way to achieve this is by creating a range object and iterating over it.


Ranges
A range is an immutable sequence type that defines a start, a stop, and a step value. The values within the range start with the beginning value and are incremented until the last value in the range is reached. This allows for ranges to be used in place of sequential lists while taking less memory and including more items.

>>> my_range = range(10)
>>> my_range
range(0, 10)
>>> list(my_range)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(1, 14, 2))
[1, 3, 5, 7, 9, 11, 13]

Notice that the "stop" value (in this example, 10) is not included in the range.

By using a range with a for loop, we can specify the number of times we would like to iterate without needing to manually worry about incrementing a counter like we had to do with a while loop. Here's a previous example where we printed "looping" four times using a while loop:

>>> count = 1
>>> while count <= 4:
...     print("looping")
...     count += 1
looping
looping
looping
looping
>>>

We could achieve this same thing using for and range like this:

>>> for _ in range(1, 5):
...     print("looping")
...
looping
looping
looping
looping
>>>