
Certified Entry-Level Python Programmer Certification


CHAPTER 14.2
The `for` Loop

We work with collections of data and sequence a lot in programming, and it is common for us to want to perform the same action on each item or a subset of items in the content. To handle this we need iteration and looping. In this lesson, we'll learn about the most common type of loop that we will use: the for loop.

The for Loop
The most common use we have for looping is when we want to execute some code for each item in a sequence. For this type of looping or iteration, we'll use the for loop. The general structure for a for loop is:

for TEMP_VAR in SEQUENCE:
    pass

The TEMP_VAR will be populated with each item as we iterate through the SEQUENCE, and it will be available to us in the context of the loop. After the loop finishes one iteration, then the TEMP_VAR will be populated with the next item in the SEQUENCE, and the loop's body will execute again. This process continues until we either hit a break statement or we've iterated over every item in the SEQUENCE. Here's an example that loops over a list of colors:

>>> colors = ['blue', 'green', 'red', 'purple']
>>> for color in colors:
...     print(color)
...
blue
green
red
purple
>>> color
'purple'

Other Iterable Types
Lists will be the most common type that we iterate over using a for loop, but we can also iterate over other sequence types. Of the types we already know, we can iterate over strings, dictionaries, and tuples.

Here's a tuple example:

>>> point = (2.1, 3.2, 7.6)
>>> for value in point:
...     print(value)
...
2.1
3.2
7.6
>>>

In this dictionary example, by default, will first unpack each key:

>>> ages = {'kevin': 59, 'bob': 40, 'kayla': 21}
>>> for key in ages:
...     print(key)
...
kevin
bob
kayla

If we leverage what we've learned about dictionaries, we can actually get the key and value on each iteration by using dict.items and unpacking the tuple in each iteration:

>>> for key, value in ages.items():
...     print(key, value)
...
kevin 59
bob 40
kayla 21

A string example:

>>> for letter in "my_string":
...     print(letter)
...
m
y
_
s
t
r
i
n
g
>>>