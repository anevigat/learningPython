
Certified Entry-Level Python Programmer Certification


CHAPTER 7.2
The `input` Function

With an understanding of the basic types in Python, we're finally ready to start writing some programs. In this lesson, we'll take a look at the input function that allows us to write command-line scripts that take in user input.


Prompting for User Input
Computer programs aren't that interesting until they can be more dynamic. Over the next few short lessons, we'll be learning about how we can receive input from a user who's running our program from the command-line, and then how we can manage to present information back to the screen.

Before we dig into the input function, let's talk a little bit about functions in general. Functions allow us to package up bits of code to be able to run them more than once. Additionally, functions specify expected inputs and can also return information. If we take a look at a function from mathematics, we can see the same thing:

f(x) = x + 2


In this case, the name of the function is f, the input is x, and the code that will be executed is x + 2. We can provide a variety of values for x and get a different return value. So f(1) would return 3. In Python, we can reference functions by name, allowing us to pass them around like variables. But a function won't be executed unless we "call it" by using parenthesis. We can see this in the REPL by typing in input without any parenthesis:

>>> input
<built-in function input>

The input function is the easiest way that we can make our programs request user interaction. This function is simple in that it only takes one optional argument to be the prompt that we present the user. Whatever the user types will be returned by the input function as a string, and that means we can store it in a variable. Let's try this out in the REPL now:

>>> favorite = input("Favorite Color: ")
Favorite Color:


Now we're left in a new prompt and we can type our answer. When we hit Enter/Return it will submit all of what we wrote and store it in the variable favorite. Note that the prompt argument is optional, so we can simply run input() without an argument and it will leave us at an empty prompt waiting once again for us to hit Enter/Return before then returning that value.

Prompting for Multiple Values
Now that we know how the input function works, let's create our first real script. In this script, we're going to ask the user to answer a series of questions, and store those answers in variables. In the next lesson, we'll then use these values.

Let's call our script bio.py, and in this script, we'll ask for the following:

The user's name
The user's favorite color
The user's age


Create and open bio.py in your text editor and call input three different times, once for each piece of information that we want:

~/code/bio.py

name = input("What is your name? ")
color = input("What is your favorite color? ")
age = input("How old are you today? ")


Both name and color make sense to be strings, but age should be a number. Let's cast the value returned from the age prompt to be an int before assigning it to the variable. We can do this by placing the parenthesis for the int function around the entire input function call:

~/code/bio.py

name = input("What is your name? ")
color = input("What is your favorite color? ")
age = int(input("How old are you today? "))


Now that we've written our script, let's run it:

$ python3.7 bio.py
What is your name? Kevin Bacon
What is your favorite color? Orange
How old are you today? 61
$


We didn't do anything with the values that were returned, but since we were returned to our shell without an error we know that everything executed properly. If we were to give an invalid answer for the age question (something that wasn't an int) Python will raise an error. We need to keep that in mind.
