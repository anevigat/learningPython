
Certified Entry-Level Python Programmer Certification


CHAPTER 9.2
List Functions and Methods

We've learned how to use some list operators to interact with our lists, but there are quite a few useful methods and functions that will make working with lists even easier.

List Methods
When it comes to lists, some methods allow us to easily achieve the same things that we previously did using operators, and in an arguably more readable way. Indexing and slicing for the sake of reading objects is easy enough, but when it comes to adding new items to a list, there are better methods.

If we want to add an object to the end of a list, then we can use the append method:

>>> my_list = [1, 2, 3]
>>> my_list.append(4)
>>> my_list
[1, 2, 3, 4]

Additionally, if we'd like to insert an item at a particular index, we can use the insert method:

>>> my_list.insert(0, 'a')
>>> my_list
['a', 1, 2, 3, 4]

Notice that we didn't replace the item that had previously been at the 0 index. We moved all items at or after the desired index, further back in the list.

If we need to know the index of an item in a list (if the item is in the list), then we have the index method:

>>> my_list = [1, 2, 3]
>>> my_list.index(2)
1
>>> my_list.index(15)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 15 is not in list

Since index raises an error, it's not something that we'll usually want to use by itself. Thankfully, there's an easy way for us to determine if an item is in a list.

The in and not in Operators
Sequence types have a few additional operators that make it easy for us to check the contents. The in and not in operators take a value that we'd like to search the sequence for on the left-hand side and a sequence on the right-hand side:

>>> my_list = [1, 2, 3]
>>> 4 in my_list
False
>>> 4 not in my_list
True
>>> 2 in my_list
True

These operators are great to use before employing the index method to ensure that we don't get a ValueError.

Helpful Functions
Besides methods, some built-in functions work great with lists. We've already seen the len function that will return the length of the list to us, but if we need to sort the contents of a list, then we have the sorted and reversed functions:

>>> my_list = [1, 3, 4, 8, 2]
>>> sorted(my_list)
[1, 2, 3, 4, 8]
>>> reversed(my_list)
<list_reverseiterator object at 0x110330d90>

The reversed function doesn't return a list, but typecasting works for the list type also, and when we have a list iterator we can turn it back into a list using the list function:

>>> reversed(my_list)
<list_reverseiterator object at 0x110330d90>
>>> list(reversed(my_list))
[2, 8, 4, 3, 1]

If we want to sort, reverse, and get a list back, we can combine all three of these functions:

>>> list(reversed(sorted(my_list)))
[8, 4, 3, 2, 1]