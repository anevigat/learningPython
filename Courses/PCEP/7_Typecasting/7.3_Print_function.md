
Certified Entry-Level Python Programmer Certification


CHAPTER 7.3
The `print` Function


Now that we've taken in some user input, we're going to look at how we can customize some information and write it out to the screen. In this lesson, we're going to dig into how the print function works, and see how we can place variable values into strings.


Printing to the Screen
In the first program that we wrote, we printed "Hello, World!" out to the screen using the print function. That's as simple as it gets, but printing in Python is incredibly easy. Now that our bio.py script is taking in some input from a user, we're ready to write some code to print information back out. Our goal is to take the information from the user for their name, color, and age and print out this sentence with the variables substituted in:

NAME is AGE years old and loves the color COLOR.
We're going to take a look at a few different ways to do this using the print function.

The print Function
As with most things in programming, there's more than one way for us to achieve our goal of printing the user's information in the proper format. For the exam, we need to understand how to use the sep and end optional arguments to the print function.

Let's take a quick look at how the print function works by default and also when we set the sep and end arguments.

~/code/bio.py

name = input("What is your name? ")
color = input("What is your favorite color? ")
age = int(input("How old are you today? "))

print(name)
print("is " + str(age) + " years old")
print("and loves the color " + color + ".")


If we run this now we'll see this:

$ python3.7 bio.py
What is your name? Kevin Bacon
What is your favorite color? Orange
How old are you today? 61
Kevin Bacon
is 61 years old
and loves the color Orange.


Every time we call print, the string will be printed to the screen with a trailing newline, so the next print will always be on the next line. We can change this by setting the end value using a keyword argument. The end argument is set to '\n' by default, but if we change it to ' ' then it should print the three lines as one. When a function takes multiple arguments, then we separate them using commas. And for keyword arguments, we use the argument's name = the value that we want it to use. We'll learn more about how arguments work for functions later, but this is enough for now.

Let's modify our script to set the end value:

~/code/bio.py

name = input("What is your name? ")
color = input("What is your favorite color? ")
age = int(input("How old are you today? "))

print(name, end=" ")
print("is " + str(age) + " years old", end=" ")
print("and loves the color " + color + ".", end=" ")


Running it again shows this:

$ python3.7 bio.py
What is your name? Kevin Bacon
What is your favorite color? Orange
How old are you today? 61
Kevin Bacon is 61 years old and loves the color Orange.


We've successfully printed out what we needed to, but it feels a little tedious. The print function can take any number of arguments before we use keyword arguments like sep and end. It will then print each argument separated by the sep character which is '' by default. If we set this to a single space then we should be able to use a single print call to print the sentence properly.

Let's see what this looks like:

~/code/bio.py

name = input("What is your name? ")
color = input("What is your favorite color? ")
age = int(input("How old are you today? "))

print(name, 'is', age, 'years old and loves the color', color, '.', sep=" ")


Running it again shows this:

$ python3.7 bio.py
What is your name? Kevin Bacon
What is your favorite color? Orange
How old are you today? 61
Kevin Bacon is 61 years old and loves the color Orange .


We're so close, but there's an extra space between the color and the period. We'll need to combine those into a single string instead.

~/code/bio.py

name = input("What is your name? ")
color = input("What is your favorite color? ")
age = int(input("How old are you today? "))

print(name, 'is', age, 'years old and loves the color', color + '.', sep=" ")