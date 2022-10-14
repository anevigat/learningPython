
Certified Entry-Level Python Programmer Certification


CHAPTER 12.2
Useful String Methods, Part 1

As strings are one of the most important and common types that we work with, we're going to dive into some different
sets of methods that we have at our disposal when working with strings. In this lesson, we'll take a look at some capitalization methods and how to evaluate the contents of a string against common patterns.

Changing String Capitalization
When working with strings, it's not uncommon for us to want to change the capitalization of the string. We can make comparisons easier or to improve the way that we display the value. Thankfully, Python provides us with simple methods on the str class for just these purposes.

>>> my_str = 'tEsTinG'
>>> my_str.lower()
'testing'
>>> my_str.upper()
'TESTING'
>>> my_str.capitalize()
'Testing'

The lower and upper methods are great for changing all of the characters in a string to either lowercase or uppercase. This is handy to do when capitalization doesn't matter and we want to compare against a value that we already know. For all intents and purposes, an email address: Kevin@example.com is the same as kevin@example.com. If we want to compare a user-provided value that could have odd capitalization with a known email address, then we could call lower before comparing the two values.

email = input("Your Email: ")
print("Email is test@example.com:", email.lower() == 'test@example.com')

The capitalize method is a little different, as it will lowercase every character besides the first one. It doesn't take into consideration if that's the right thing to do for the words within the string. Because of this, you might not find yourself using capitalize all that often, but in many cases, it will work for single-word strings.

Checking String Patterns with .is___ Methods
Since strings are collections of characters, they can hold onto an incredible variety of information. But that doesn't mean that there aren't different patterns that the information could fall into. For instance, the string '12' is completely numeric. For these types of patterns, the str class provides a whole family of methods that start with is, such as isnumeric:

>>> "12".isnumeric()
True

There are quite a few of these methods. Here's a list:

isascii - Return True if all characters in the string are ASCII, False otherwise.
islower - Return True if the string is a lowercase string, False otherwise.
isupper - Return True if the string is an uppercase string, False otherwise.
istitle - Return True if the string is a title-cased string (all words capitalized), False otherwise.
isspace - Return True if the string is a whitespace string, False otherwise.
isdecimal - Return True if the string is a decimal string (whole number), False otherwise.
isdigit - Return True if the string is a digit string (whole number), False otherwise.
isnumeric - Return True if the string is a numeric string (whole number), False otherwise.
isalpha - Return True if the string is an alphabetic string, False otherwise.
isalnum - Return True if the string is an alphanumeric string, False otherwise.
isidentifier - Return True if the string is a valid Python identifier, False otherwise. String could be used as a variable, function, or class name.
isprintable - Return True if the string is printable, False otherwise. Meaning that if the character can't be printed as-is, then it's not printable. So escape characters like \n are considered not printable even though they change how the string is printed.