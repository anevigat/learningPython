
Certified Entry-Level Python Programmer Certification


CHAPTER 13.2
Handling Multiple Cases with `elif`

Being able to perform one thing or another based on a condition is useful. But there are many situations where we want to check multiple possible conditions, and have more than two possible branches. In this lesson, we'll learn about how we can use the elif statement to have multiple branching paths in our conditionals.

The elif Statement
When we want our programs to have more than two possible outputs, then the elif statement will work perfectly for us. The elif statement looks a lot like the if statement:

if CONDITION:
   # do something
elif CONDITION_2:
   # do a different thing
else:
   # do something if all conditions are False


We can chain as many elif statements together as we need, so the number of cases that we can handle is effectively limitless. Let's put elif to use by creating a script to evaluate the length of a name provided when we run the script:

learning-conditionals.py

name = input("What is your name? ")
if len(name) >= 6:
   print("Your name is long.")
elif len(name) == 5:
   print("Your name is 5 characters.")
elif len(name) >= 4:
   print("Your name is 4 or more characters.")
else:
   print("Your name is short.")

When we run this, we can see the various results:

$ python3.7 learning-conditionals.py
What is your name? Keith
Your name is 5 characters.
$ python3.7 learning-conditionals.py
What is your name? Alex
Your name is 4 or more characters.
$ python3.7 learning-conditionals.py
What is your name? Alex
Your name is 4 or more characters.
$ python3.7 learning-conditionals.py
What is your name? Bob
Your name is short.
$ python3.7 learning-conditionals.py
What is your name? Cynthia
Your name is long.

Notice that we fell into the first elif statement's block, and then the second elif block was never executed even though it was true. We can only exercise one branch in an if statement.
