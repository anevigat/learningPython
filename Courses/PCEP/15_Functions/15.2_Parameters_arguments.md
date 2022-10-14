
Certified Entry-Level Python Programmer Certification


CHAPTER 15.2
Parameters vs. Arguments

When talking about functions, the words "parameter" and "argument" are often used interchangeably. But they represent two different things. In this lesson, we'll look at the differences between parameters and arguments, and the different ways we can use arguments when calling functions.

Parameters VS Aruguments
The difference between a parameter and an argument is all about timing. When we're working with the definition of a function, then the variables defined in the function declaration are the "parameters." When we're calling the function, the data that we provide for each parameter is the "argument." Accidentally using these words interchangeably in practice isn't an issue, because other programmers will know exactly what you're talking about. But it is good to know that there is a distinction.

With the semantic differences covered, we're ready to move onto the more interesting topic of the various types of arguments that we can use: position and keyword arguments.

Using Keyword Arguments
Every function call we've made up to this point has used what are known as positional arguments. But if we know the name of the parameters, and not necessarily the positions, we can all them all using keyword arguments like so:

>>> def contact_card(name, age, car_model):
...     return f"{name} is {age} and drives a {car_model}"
...
>>> contact_card("Keith", 29, "Honda Civic")
'Keith is 29 and drives a Honda Civic'
>>> contact_card(age=29, car_model="Civic", name="Keith")
'Keith is 29 and drives a Civic'
>>> contact_card("Keith", car_model="Civic", age="29")
'Keith is 29 and drives a Civic'
>>> contact_card(age="29", "Keith", car_model="Civic")
  File "<stdin>", line 1
SyntaxError: positional argument follows keyword argument

When we're using position and keyword arguments, every argument after the first keyword argument must also be a keyword argument. It's sometimes useful to mix them, but oftentimes we'll use either all positional or all keyword.

Defining Parameters with Default Arguments
Along with being able to use keyword arguments when we're calling a function, we're able to define default values for parameters to make them optional when the information is commonly known and the same. To do this, we use the assignment operator (=) when we're defining the parameter:

>>> def can_drive(age, driving_age=16):
...     return age >= driving_age
...
>>> can_drive(16)
True
>>> can_drive(16, driving_age=18)
False

Parameters with default arguments need to go at the end of the parameters list when defining the function so that positional arguments can still be used to call the function.
