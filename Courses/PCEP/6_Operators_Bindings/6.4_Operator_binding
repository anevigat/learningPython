
Certified Entry-Level Python Programmer Certification


CHAPTER 6.4
Operator Priority (Binding)

Now that we've learned about quite a few operators, we're ready to learn how Python determines the order to run them if there are multiple in a single expression.


Operator Precedence
In mathematics, we have the order of operations that tell us how we're going perform our calculations, and in Python, we have operator precedence. We haven't covered all of the contents of this table just yet, but we can look at how everything that we have used so far will be processed.

For whatever reason, the Python documentation shows the least binding operators first, but we'll talk about them from most binding to least. We'll leave the ones that we won't cover in this course out of the list though:

Parenthesis and List/Dictionary/Set literals
Accessing attributes (subscription, slicing, function/method call, attribute reference)
Exponentiation (**)
Positive, Negative, and bitwise complement
Multiplication *, Division /, Floor Division //, Modulo %
Addition +, Subtraction -
Bitwise Shifts << & >>
Bitwise AND &
Bitwise XOR ^
Bitwise OR |
Comparison operators (in, not in, is, is not, <, >, <=, >=, ==, !=)
Boolean NOT not
Boolean AND and
Boolean OR or
Conditions if


Let's look at some examples:

>>> 14 & 3 * 2 + 4
10
>>> 14 & 3 * (2 + 4)
2
>>> (14 & 3) * 2 + 4
8
>>> 14 & (3 * 2) + 4
10