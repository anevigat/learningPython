
Certified Entry-Level Python Programmer Certification


CHAPTER 14.4
Controlling Loop Execution with `break` and `continue`

There are times while working with loops, that we want to skip a single iteration, or even completely stop a loop before it is finished. We can accomplish these two things by using the continue and break statements.

The continue and break Statements
If we want to continue to the next iteration in a nested context or stop the loop entirely, we have access to the continue and break keywords:

>>> count = 0
>>> while count < 10:
...     if count % 2 == 0:
...         count += 1
...         continue
...     print(f"We're counting odd numbers: {count}")
...     count += 1
...
We're counting odd numbers: 1
We're counting odd numbers: 3
We're counting odd numbers: 5
We're counting odd numbers: 7
We're counting odd numbers: 9
>>>

The continue statement will cause the nearest loop (if we have nested loops) to go directly to the next iteration. This means that we will not execute any of the remaining lines of the loop for the current iteration. This can be an issue if we continue without incrementing the count value in our example loop's conditional.

We're demonstrating "string interpolation" in Python 3 by prefixing a string literal with an f and then using curly braces to substitute in variables or expressions (in this case, the count value).

The break statement works similarly to the continue statement in that it keeps our current iteration from executing the remaining lines in the loop, but it also causes the entire loop to stop.

Here's an example using the break statement:

>>> count = 1
>>> while count < 10:
...     if count % 2 == 0:
...         break
...     print(f"We're counting odd numbers: {count}")
...     count += 1
...

We're counting odd numbers: 1
Using break and continue with a for Loop
The break and continue statements work with for loops as well. If we didn't want to print out certain colors, we could utilize the continue or break statements again. Let's say we want to skip the string 'blue' and terminate the loop if we see the string 'red':

>>> colors = ['blue', 'green', 'red', 'purple']
>>> for color in colors:
...     if color == 'blue':
...         continue
...     elif color == 'red':
...         break
...     print(color)
...
green
>>>