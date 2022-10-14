
Certified Entry-Level Python Programmer Certification


CHAPTER 17.1
Python Scopes

We've lightly touched on this already, but when working with any programming language, the variables and objects that we're working with are only accessible within certain scopes. In this lesson, we'll take a closer look at how scopes work and when our variables might not be what we expect them to be.

What is a Scope?
When we say that we're working in a different "scope" in Python, we mean that we're within the boundaries of a function or a class. This is important because while within the body of a function or class, the variables that we create are not automatically accessible outside of that context. Let's create a new file called scopes.py so that we can experiment with how scopes work. To start, let's see how variables work when dealing with conditionals and loops.

scopes.py

if 1 < 2:
    x = 5

while x < 6:
    print(x)
    x += 1

print(x)

Here we're creating a variable (x=5) within the body of a conditional (if 1 < 2:1). Afterward, we attempt to access that variable within the context of a loop (while x < 6:) and at the highest level of our script. Will this work? Let's find out by running this through the interpreter:

$ python3.7 scopes.py
5
6
$

We didn't run into an error because conditionals and loops do not create scopes. Now, let's change our conditional to be a function instead.

scopes.py

def set_x():
    x = 5

set_x()

while x < 6:
    print(x)
    x += 1

print(x)

Now if we run this we'll see the following:

$ python3.7 scopes.py
Traceback (most recent call last):
  File "scopes.py", line 7, in <module>
    while x < 6:
NameError: name 'x' is not defined
$

We see this error because x is defined within the set_x function and only exists during the execution of the function.
