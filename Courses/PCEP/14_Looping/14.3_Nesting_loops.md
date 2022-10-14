
Certified Entry-Level Python Programmer Certification


CHAPTER 14.3
Nesting Loops and Conditionals

Now that we've learned how to use loops and conditionals, we can do a lot more with our programs. We can do even more when we combine them by nesting loops within conditionals or conditionals within loops.

Nesting Conditionals within Loops
We've seen two of the most common types of code contexts in Python: the body of a conditional and the body of a loop. To signify code contexts in Python, we use indentation. If we need to nest contexts, like conditionals or loops, then we can add more indentation. Let's say we're looping through a list of numbers, and we only want to print the number if it's a multiple of 4. In this case, we can add a conditional check within our loop:

>>> counter = 1
>>> while counter <= 25:
...     if counter % 4 == 0:
...         print(counter)
...     counter += 1
...
4
8
12
16
20
24

For each nested context, we'll need to indent an extra 4 spaces. When we're done doing what we need to do in a nested context, then we go back to the previous indentation level to continue at that level. This is how we're able to continue past the if statement to increment the counter, all still within the while loop.
