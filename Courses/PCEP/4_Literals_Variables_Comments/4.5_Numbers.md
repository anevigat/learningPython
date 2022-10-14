
Certified Entry-Level Python Programmer Certification


CHAPTER 4.5
Numbers: Integers, Floats, and Scientific Notation

Let's learn about some of the core data types in Python: the number types int and float.

Documentation For This Video
numeric types (the int and float types) (https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)


Numbers
There are two main types of numbers that we'll use in Python, int and float. The big difference between an int and a float being that the float class handles decimal point information.

If either of the numbers in a mathematical operation in Python is a float, then the other will be converted before carrying out the operation and the result will always be a float.

Scientific notation
If we happen to be working with really large numbers, and it's easier to use scientific notation, then Python can help us. For the equivalent of a float times 10 to a specified power we're able to use e or E when specifying the number:

>>> 4.5e9
4500000000.0
>>> 4.5e9 == 4.5 * (10 ** 9) == 4.5E9 == 4.5E+9
True