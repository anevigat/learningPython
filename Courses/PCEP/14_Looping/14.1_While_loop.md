
Certified Entry-Level Python Programmer Certification


CHAPTER 14.1
The `while` Loop

We work with collections of data and sequence a lot in programming, and it is common for us to want to perform the same action on each item or a subset of items in the content. To handle this, we need iteration and looping. In this lesson, we'll learn about one type of loop that we can use: the while loop.

The while Loop
The most basic type of loop that we have at our disposal is the while loop. This type of loop repeats itself based on a condition that we pass to it. Here's the general structure of a while loop:

while CONDITION:
    pass

The CONDITION in this statement works the same way that it does for an if statement. When we demonstrated the if statement, we first tried it by simply passing in True as the condition. Let's see when we try that same condition with a while loop:

>>> while True:
...     print("looping")
...
looping
looping
looping
looping

That loop will continue forever, we've created an infinite loop. To stop the loop, press Ctrl-C. Infinite loops are one of the potential problems with while loops. If we don't use a condition that we can change from within the loop, then it will continue forever if it's initially true. Here's how we'll normally approach using a while loop, where we modify something about the condition on each iteration:

>>> count = 1
>>> while count <= 4:
...     print("looping")
...     count += 1
...
looping
looping
looping
looping
>>>