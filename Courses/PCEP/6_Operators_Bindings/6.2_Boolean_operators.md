
Certified Entry-Level Python Programmer Certification


CHAPTER 6.2
Boolean Operators

Believe it or not, now that we understand bitwise operators we've learned the basics of doing boolean logic. We're in a great spot to learn about boolean operators.

The not Operation
Sometimes we want to know the opposite boolean value for something. To do this, we use the unary operators not:

>>> not True
False
>>> not False
True


The or Operation
The boolean or operator works the same way that the bitwise OR operator did if we are only considering one bit. The bit of 1 is equivalent to True and 0 is equivalent to False

>>> True or True
True
>>> True or False
True
>>> False or False
False
>>> False or True
True


The and Operation
The and operator is the opposite of or, and both of the operands need to be true.

>>> True and True
True
>>> True and False
False
>>> False and False
False
>>> False and True
False