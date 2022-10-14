
Certified Entry-Level Python Programmer Certification


CHAPTER 9.1
Lists

In Python, there are a few different sequence types that we're going to work with, the most common of which is the list type. In this lesson, we'll go through how we can create and modify lists.

Lists
We create a list in Python by using the square brackets ([]) and separating the values with commas. Here's an example list:

>>> my_list = [1, 2, 3, 4, 5]

For standard use, there's not a limit to how long our list can be. Lists are a heterogeneous collection type, so the items within the list do not all need to be of the same type:

>>> other_list = ['a', 1, 1.0, False]

Reading from Lists
To access an individual element of a list, we index it the same way that we would for a character in a string:

>>> my_list[0]
1
>>> my_list[2]
2

If we try to access an index that is too high (or too low) then we'll receive an error:

>>> my_list[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range

To make sure that we're not trying to get an index that is out of range, we can test the length using the len function (and then subtract 1):

>>> len(my_list)
5

Additionally, we can access subsections of a list by "slicing" it. We provide the starting index and the ending index (the object at that index won't be included):

>>> my_list[0:2]
[1, 2]
>>> my_list[1:0]
[2, 3, 4, 5]
>>> my_list[:3]
[1, 2, 3]
>>> my_list[0::1]
[1, 2, 3, 4, 5]
>>> my_list[0::2]
[1, 3, 5]

Modifying a List
Unlike strings, which can't be modified (we can't change a character in a string), we can change a value in a list using the subscript equals operation:

>>> my_list[0] = "a"
>>> my_list
['a', 2, 3, 4, 5]

Lists can be added together (concatenated). This operation will return a new list, but we can use the += compound operator to add items to the end of our lists:

>>> my_list + [8, 9, 10]
['a', 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> my_list += [8, 9, 10]
>>> my_list
['a', 2, 3, 4, 5, 6, 7, 8, 9, 10]

Items in lists can be set using slices as well:

>>> my_list[1:3] = ['b', 'c']
>>> my_list
['a', 'b', 'c', 4, 5, 6, 7, 8, 9, 10]

Slicing and assigning can still be used if the slice size is smaller than the list being assigned. This will insert additional elements:

>>> my_list[3:5] = ['d', 'e', 'f']
>>> print(my_list)
['a', 'b', 'c', 'd', 'e', 'f', 6, 7, 8, 9, 10]

We can remove a section of a list by assigning an empty list to the slice:

>>> my_list = ['a', 'b', 'c', 'd', 5, 6, 7]
>>> my_list[4:] = []
>>> my_list
['a', 'b', 'c', 'd']

Removing Items from a List
Another way that we can remove an item from a list is by using the del statement and the indexing operation:

>>> my_list = ['a', 'b', 'c', 'd']
>>> del my_list[0]
>>> my_list
['b', 'c', 'd']

One thing to note about del is that it will remove the entire list variable if we don't pass it an index:

>>> del my_list
>>> my_list
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'my_list' is not defined