
Certified Entry-Level Python Programmer Certification


CHAPTER 12.3
Useful String Methods, Part 2

As strings are one of the most important and common data types that we work with, we're going to dive into some different
sets of methods that we have at our disposal when working with strings. In this lesson, we'll take a look at how to split strings apart, build them up from a list, and substitute information into a string using the format method.

Splitting and Joining Strings
Sometimes we have strings that we want to break into smaller pieces to work with. If we have a delimiter that we'd like to use to separate the string into smaller strings, then we're able to use the split method to get a list of substrings. A simple example of this would be getting the individual words in a string by splitting on a single space (the default separator):

>>> phrase = "This is a simple phrase"
>>> words = phrase.split()
>>> words
['This', 'is', 'a', 'simple', 'phrase']

Another way I've personally used this is to get the final segment of a URL by splitting on slashes and then selecting the last item in the list:

>>> url = 'https://example.com/users/jimmy
>>> user = url.split('/')[-1]
>>> user
'jimmy'

Being able to split a string is useful, but we might also want to create a single string from a list of strings that we already have. To do this we can use the join method. It's interesting because the string we start with will be the separator that we want inserted between the strings in the list. Let's take our words list and insert commas between the words instead of spaces:

>>> phrase = "This is a simple phrase"
>>> words = phrase.split()
>>> ", ".join(words)
'This, is, a, simple, phrase'

A common way that join is used is by taking a list of lines forming them into a single string with new lines between the lines:

>>> lines = ['First line', 'Second line', 'Third line']
>>> output = '\n'.join(lines)
>>> print(output)
First line
Second line
Third line

Formatting Strings with format
The last method that we're going to talk about is the format method. We often have a good idea of what a message needs to look like, but we want to have some dynamic information inserted into the middle of a string. Up to this point, we've been using the multiple arguments available to the print function, but sometimes we don't want to print the formatted string out.

The format method allows us to place {} segments into a string and then have values added into those positions:

>>> "Hello, my name is {}, and I really enjoy {}. Have a nice day!".format('Keith', 'Python')
'Hello, my name is Keith, and I really enjoy Python. Have a nice day!'

If we want to use the same value multiple times within the string, then we can place the item index within the {} values:

>>> "Hello, my name is {0}, and I really enjoy {1}. Have a nice day! - {0}".format('Keith', 'Python')
'Hello, my name is Keith, and I really enjoy Python. Have a nice day! - Keith'

It's worth noting that these two approaches can't be mixed. There's a lot more that we can do with the format method, and reading the Format String Syntax documentation can help.