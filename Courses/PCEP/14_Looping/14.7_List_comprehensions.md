
Certified Entry-Level Python Programmer Certification


CHAPTER 14.7
List Comprehensions

Iterating over a sequence is great, but needing to transform a list into a different list is fairly common. Python has a special feature to make doing this concise, called "list comprehensions".


List Comprehensions
If we want to loop through a list, modify each item, and have a new list with the modified items, then we could do something like this:

>>> colors = ['red', 'blue', 'orange', 'green', 'yellow']
>>> uppercase_colors = []
>>> for color in colors:
...     uppercase_colors.append(color.upper())
...
>>> uppercase_colors
['RED', 'BLUE', 'ORANGE', 'GREEN', 'YELLOW']

This procedure is common enough that Python provides a shorthand method for doing it in the form of "list comprehensions." These have a unique syntax where we essentially put the for loop within square brackets ([]). Here's the equivalent for the above, using a list comprehension:

>>> colors = ['red', 'blue', 'orange', 'green', 'yellow']
>>> uppercase_colors = [color.upper() for color in colors]
>>> uppercase_colors
['RED', 'BLUE', 'ORANGE', 'GREEN', 'YELLOW']

The biggest difference here is that we don't need to create an empty list and append to it. Whatever we place to the left of the for statement within the comprehension will be returned as part of the final list.

List Comprehensions for Filtering
List comprehensions also have another feature that allows for filtering while iterating through the initial list by adding a trailing if statement within the square brackets ([]). If we wanted to iterate through our colors and only return "warm" colors (red, orange, yellow) then we could write this loop to achieve these results:

>>> colors = ['red', 'blue', 'orange', 'green', 'yellow']
>>> warm_colors = []
>>> for color in colors:
...     if color in ['red', 'orange', 'yellow']:
...         warm_colors.append(color.upper())
...
>>> warm_colors
['RED', 'ORANGE', 'YELLOW']

If we remove the concept of warm_colors being used within the loop, we can write it as a list comprehension:

>>> colors = ['red', 'blue', 'orange', 'green', 'yellow']
>>> warm_colors = [color.upper() for color in colors if color in ['red', 'orange', 'yellow']]
>>> warm_colors
['RED', 'ORANGE', 'YELLOW']

The syntax for list comprehensions are a little odd to get started with. But if you read it as a sentence, then it will start to make more sense and feel more useful. The sentence would read something like this: Uppercase each color in the colors variable if the colors are red, orange, and yellow.
