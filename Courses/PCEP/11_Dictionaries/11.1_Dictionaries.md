
Certified Entry-Level Python Programmer Certification


CHAPTER 11.1
Dictionaries

Learn how to use dictionaries (the dict type) to hold onto key/value information in Python.

Dictionaries
Dictionaries are the main mapping type that we'll use in Python. This object is comparable to a Hash or "associative array" in other languages.

Things to note about dictionaries:

Unlike Python 2 dictionaries, Python 3.7 keys are ordered in dictionaries. We will need OrderedDict if we want this to
work on another version of Python.
You can set the key to any IMMUTABLE TYPE (no lists).
Avoid using things other than simple objects as keys.
Each key can only have one value (so we don't have duplicates when creating with dict).

We create dictionary literals by using curly braces ({ and }), separating keys from values using colons (:), and separating key/value pairs using commas (,). Here's an example dictionary:

>>> ages = { 'kevin': 59, 'alex': 29, 'bob': 40 }
>>> ages
{'kevin': 59, 'alex': 29, 'bob': 40}

We can read a value from a dictionary by subscripting using the key:

>>> ages['kevin']
59
>>> ages['billy']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'billy'

Keys can be added or changed using subscripting and assignment:

>>> ages['kayla'] = 21
>>> ages
{'kevin': 59, 'alex': 29, 'bob': 40, 'kayla': 21}

Items can be removed from a dictionary using the del statement:

>>> del ages['kevin']
>>> ages
{'alex': 29, 'bob': 40, 'kayla': 21}
>>> del ages
>>> ages
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'ages' is not defined

The in and not in Operators
Just like with lists and tuples, dictionaries have access to the in and not in operators. Notably, this only considers the keys:

>>> ages = {'kevin': 59, 'bob': 40}
>>> 'kevin' in ages
True
>>> 59 in ages
False

Alternative Ways to Create a dict Using Keyword Arguments
There are a few other ways to create dictionaries that we might see, which are those using the dict constructor with key/value arguments and a list of tuples:

>>> weights = dict(kevin=160, bob=240, kayla=135)
>>> weights
{'kevin': 160, 'bob': 240, 'kayla': 135}
>>> colors = dict([('kevin', 'blue'), ('bob', 'green'), ('kayla', 'red')])
>>> colors
{'kevin': 'blue', 'bob': 'green', 'kayla': 'red'}