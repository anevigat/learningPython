
Certified Entry-Level Python Programmer Certification

CHAPTER 4.2
Variables and the Assignment Operator

Almost any script that we write will need to provide a way for us to hold onto information for use later on. That's where variables come into play.

Working with Variables
We can assign a value to a variable by using a single = and we don't need to (nor can we) specify the type of the variable.

>>> my_str = "This is a simple string"


Now we can print the value of that string by using my_var later on:

>>> print(my_str)
This is a simple string


We can also change the value that is assigned to a variable later on, either by using the standard assignment operator = or by using some of the short-hand operators that we'll learn about as we continue.

>>> my_str += " testing"
>>> my_str
'This is a simple string testing'


An important thing to realize is that the contents of a variable can be changed and we don't need to maintain the same type:

>>> my_str = 1
>>> print(my_str)
1


Ideally, we wouldn't change the contents of a variable called my_str to be an interger, but it is something that Python will allow us do.

One last thing to remember is that, if we assign a variable with another variable, it will be assigned to the initial result of the variable and not whatever that variable points to later.

>>> my_str = 1
>>> my_int = my_str
>>> my_str = "testing"
>>> print(my_int)
1
>>> print(my_str)
testing


Short-Hand Assignment Operators
There are numerous shorthand assignment operators we can use that allow us to perform operations and also assign back to variables in the way that we did with the += operator. The form for these shorthand assignment operations always follows the same pattern. We'll take the operator that we want to use, say +, and create a new operator by adding = to the right-hand side of it. So, for the subtraction operation, we could subtract from the current value and assign the new value to a variable using the -= operator.

As we learn about more and more operators we'll be able to follow this pattern if we want to reassess our current variable based on an operation.