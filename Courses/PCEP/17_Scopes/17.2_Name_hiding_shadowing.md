
Certified Entry-Level Python Programmer Certification


CHAPTER 17.2
Name Hiding (Shadowing)

Now that we've looked at how scopes work initially, we're ready to look at what happens when we have a function
parameter that is the same as a variable that exists at a higher level. This is sometimes called shadowing or name hiding.

Name Hiding in Action
We know that functions create scopes. But, what happens when a parameter name is the same as a variable that has already been defined? Let's continue using scopes.py to see what happens when we set y before we define the set_x function, and then change our function to have a y parameter:

scopes.py

y = 5

def set_x(y):
    print("Inner y:", y)
    x = y
    y = x

set_x(10)
print("Outer y:", y)

Now if we run this, we'll see the following:

$ python3.7 scopes.py
Inner y: 10
Outer y: 5

Since our function defines the y parameter, it's as though the outer y variable doesn't exist within the set_x function. Name hiding makes it possible for us to be confident that our parameters won't be affected by values at a higher scope. That doesn't mean that name hiding is something that we should always use though because it can make our code a little harder for people to understand.
