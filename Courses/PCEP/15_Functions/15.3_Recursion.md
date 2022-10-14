
Certified Entry-Level Python Programmer Certification


CHAPTER 15.3
Recursion

It might not seem immediately obvious, but we're capable of calling a function from within itself. This practice is called recursion. In this lesson, we'll learn how we can use recursion and some of the pitfalls that surround it.


Solving Problems with Recursion
Recursion is the practice of calling a function from within itself. This might not seem like something that you'd ever do at first, but occasionally the best way to solve a problem is to break it up into smaller versions of the same problem. The canonical example of this is calculating the Fibonacci Sequence (1, 1, 2, 3, 5, 8, etc.). In the Fibonacci sequence, the next number is always the sum of the previous two numbers in the sequence. If we write this out as a mathematical function, then calculating the nth item in the Fibonacci sequence would look something like this:

f(n) = f(n-2) + f(n-1)

So, for the 5th item in the sequence (which coincidently is also 5), we would expand it like this:

f(5) = f(3) + f(4)
f(5) = f(1) + f(2) + f(2) + f(3)
f(5) = 1 + f(0) + f(1) + f(0) + f(1) + f(1) + f(2)
f(5) = 1 + 0 + 1 + 0 + 1 + 1 + f(0) + f(1)
f(5) = 1 + 0 + 1 + 0 + 1 + 1 + 0 + 1
f(5) = 5

For recursion to work, there has to be what is called a "base case," where something is returned other than the result of the function calling itself. In the case of our Fibonacci sequence function, the base case(s) are that f(0) will return 0, and f(1) will return 1. Now that we can visualize exactly what is going on, let's write this function in Python:

~/fib.py

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fib(n - 2) + fib(n - 1)

item_to_calculate = int(input("What Fibonnaci item would you like to calculate? "))

print(fib(item_to_calculate))

In writing our function, we needed to remember a few things:

We need to handle the base cases first.
We return what we would normally consider the implementation of the function. This return allows us to essentially gather all of the results at the end.
Let's run our script:

$ python3.7 fib.py

What Fibonacci item would you like to calculate? 15
610

That was pretty fast, but as we increase the number from 15 to 30, we should see it take significantly longer to return. This is because the number of recursive function calls that happen as we try to calculate higher and higher terms gets excessively large. Trying to calculate the 50th term using our implementation might not ever return.

The Limits of Recursion
We've run into the main issue with recursion, every time we recurse it, we're adding more and more function calls to the stack of calls that need to be completed. Some languages are optimized to handle this by implementing something called "tail-call optimization," but Python is not one of those languages. Recursion is a useful tool at times, but it does require being delicate and layering in some manual optimization (which we won't be covering here).
