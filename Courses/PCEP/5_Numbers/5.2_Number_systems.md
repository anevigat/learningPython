
Certified Entry-Level Python Programmer Certification


CHAPTER 5.2
Number Systems

In our day to day work, we almost always work with decimal numbers. These are not necessarily numbers with decimal points, but numbers derived from a base 10 number system. In this lesson, we'll take a look at how we could use other number systems in Python.

What are Number Systems?
We normally count using the decimal number system, which means that for each digit in a number we will cycle between the numbers 0-9 before adding another digit. These same numbers can be represented using other numbering systems though, such as binary which only uses the number 0-1.

The decimal number of 15 is equivalent to 1111 in binary notation. To convert from decimal to binary we divide the decimal number (15) by the base of the other numbering system, in binary's case that's 2 and then we take the remainder as a digit in the binary number. We then take the part that divided cleanly and divide it by the base again. Here's the process for converting 15 to binary:

15 / 2 => 7 w/ remainder of 1
7 / 2 => 3 w/ remainder of 1
3 / 2 => 1 w/ remainder of 1
1 / 2 => 0 w/ remainder of 1

If we do this with the number 12 we'll get something different:

12 / 2 => 6 w/ remainder of 0
6 / 2 => 3 w/ remainder of 0
3 / 2 = 1 w/ remainder of 1
1 / 2 = 0 w/ remainder of 1

The bits go from least significant to most, so the remainders at the end of our division will be the most significant digits. 12 as binary is 1100.

Converting back to decimal requires us to multiply each bit from least to greatest by the base (2 in binary) to the power of it's position (starting with the 0 power) and then add those numbers together. Converting 1100 back to decimal looks like this:

(1 * 2 ^ 3) + (1 * 2 ^ 2) + (0 * 2 ^ 1) + (0 * 2 ^ 0)
(1 * 8) + (1 * 4) + (0 * 2) + (0 * 1)
8 + 4 + 0 + 0
12


Common Numeral Systems
The most common numbering systems are decimal (10), binary (2), octal (8), and hexadecimal (16). You might be asking yourself, "How do I represent a digit with 16 different numbers?". That's a reasonable question. The answer is to start using letters in addition to numbers. Hexadecimal digits go from 0-9, then from A-F. The binary number 12 is C in Hexadecimal.

Representing Binary, Octal, and Hexadecimal Numbers in Python
Now that we know how various and common number systems work let's go about actually using them in Python. To represent a number in a different number system in Python, we do this by prefixing the number with a 0 and the number system identifier:

Binary uses b
Octal uses o
Hexadecimal uses x


Here are examples in the REPL:

>>> 0b1001
9
>>> 0o7424
3860
>>> 0xFF012
1044498


The result printed out will be the decimal value. If we want to work in decimal values and represent them in a different numbering system we can use the bin, oct, and hex functions like so:

>>> bin(10)
'0b1010'
>>> oct(59)
'0o73'
>>> hex(1024)
'0x400'


The value returned from these functions will always be a string.
