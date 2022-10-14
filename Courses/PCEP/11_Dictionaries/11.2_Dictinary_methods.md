
Certified Entry-Level Python Programmer Certification


CHAPTER 11.2
Dictionary Methods

The dict type has plenty of useful methods that we should know, in order to make them even more useful in our code. This lesson illustrates the main methods that we'll use:

keys
values
items

Dictionary Methods
When we're working with dictionaries, we often need to perform actions on all of the keys, all of the values, or each pair (item). Thankfully the keys, values, and items methods each return something to make this easier. Let's take a look at the key method first:

>>> ages = {'kevin': 61, 'bob': 79}
>>> ages.keys()
dict_keys(['kevin', 'bob'])


Take notice of the return value, it's a dict_keys item. This by itself may not seem useful, but it can be cast to a list if that type makes more sense for what we're doing:

>>> list(ages.keys())
['kevin', 'bob']


We'll also follow this pattern for both values and items:

>>> ages.values()
dict_values([61, 79])
>>> list(ages.values())
[61, 79]
>>> ages.items()
dict_items([('kevin', 61), ('bob', 79)])
>>> list(ages.items())
[('kevin', 61), ('bob', 79)]


Because each item in a dictionary is a key and value, the result of items (when typecast to a list) is a list of 2-tuples (often called "pairs"). This is a good example of using a tuple, because we know these items will always be two items long.

As we learn about iterating, these methods will become incredibly valuable for doing useful things with dictionaries.
