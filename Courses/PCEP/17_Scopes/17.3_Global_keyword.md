
Certified Entry-Level Python Programmer Certification


CHAPTER 17.3
The `global` Keyword

Occasionally, we want to be able to modify a global variable from within a more specific context. In this situation, Python provides us with the global keyword. In this lesson, we'll learn how to use the global keyword.

Modifying the Global State from a Nested Scope
If we would like one of our functions to have the side effect of changing or creating a global variable, we can utilize the global statement. This isn't something that we'll use all that often since it is better to keep global state to a minimum as we start working on larger and more complex programs. But it is useful now and then. Let's modify scopes.py so that we can change the global y variable from within our set_x function:

scopes.py

y = 5

def set_x(y):
    print("Inner y:", y)
    x = y
    global y
    y = x


set_x(10)
print("Outer y:", y)

If we run this, we should see the following:

python3.7 scopes.py
  File "scopes.py", line 7
    global y
    ^
SyntaxError: name 'y' is parameter and global

It's important to know that we can't utilize the global statement if we have a parameter with the same name. Let's change our parameter to be z before running this again:

scopes.py

y = 5

def set_x(z):
    x = z
    global y
    global a
    y = x
    a = 7

print("y Before set_x:", y)
set_x(10)
print("y After set_x:", y)
print("a After set_x:", a)

We've also created a global variable from within our set_x function called a. This variable won't be available before the first time that set_x is called, but we should be able to print it after we've called our function for the first time. Let's run scopes.py again:

$ python3.7 scopes.py
y Before set_x: 5
y After set_x: 10
a After set_x: 7

This example shows how potentially confusing using global can be. We have a function called set_x that will change the global state for the variable y. Someone who didn't write this code could be completely confused as to why the value of the variable y that they've been working with was changed right out from under them. Keep this in mind when considering whether or not it's a good idea to use the global statement.
