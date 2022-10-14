
Certified Entry-Level Python Programmer Certification


CHAPTER 8.3
String Indexing and Slicing

Sometimes we need to access a specific item, or a subset of items, in a sequence. To do that in Python,
we'll use indexing and slicing.

Indexing
When we need to access a single item from a sequence, like a string, we'll use "indexing." Every item in a sequence type has an index that indicates the item's position in the sequence. The first item in a Python sequence has the index of 0, and each subsequent item's index increases by one. To perform indexing, we'll use square brackets ([ and ]) on the right-hand side of our string (or string variable), and within the square brackets we'll put the index number that we'd like to access:

>>> test_str = 'testing'
>>> test_str[0]
't'

There isn't a character type in Python, so the return value will be a length one string. When indexing a string, the index must exist, otherwise, Python will raise an error:

>>> test_str[10]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range

This is one of the areas where using len can help us avoid using an index that is too high. But since the starting index is 0, then the final index will always be len(test_str) - 1:

>>> test_str[len(test_str) - 1]
'g'

If we try to use a negative index, it will actually start giving us items relative to the end of the string:

>>> test_str[-1]
'g'
>>> test_str[-4]
't'
>>> test_str[-8]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range

Slicing
If we want to get a subsection of our string then we'll do what is called slicing. Slicing allows us to specify the index of the first element that we would like, followed by the index just beyond the last item that we'd like. We separate these indexes by using a colon (:)

>>> test_str[0:2]
'te'
>>> test_str[3:5]
'ti'

If we'd like to get all of the items after our starting index then we can use the length of the string as our second index, even though it's technically out of range. Or we can simply put nothing after the colon:

>>> test_str[2:len(test_str)]
'sting'
>>> test_str[2:]
'sting'

The last thing to mention about slicing is that there is a third number that we can use: the "step" value. By default, this value is 1 and just means that we'll go one-by-one through the sequence. But we can change this to grab every other item if we'd like by adding a second colon and the step size that we'd like to use:

>>> test_str
'testing'
>>> test_str[1:5:2]
'et'
>>> test_str[1::2]
'etn'

One neat thing that we can do with this step option is stepping backward by using a negative step value. We can reverse an entire string by leaving off the start and end indexes and setting the step value to -1:

>>> test_str[::-1]
'gnitset'