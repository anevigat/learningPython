
Certified Entry-Level Python Programmer Certification


CHAPTER 9.3
Nested Lists: Matrices and Cubes

Lists are a heterogeneous data structure and can hold onto a variety of data types, this includes other lists. In this lesson, we'll take a look at how we can model matrices in Python by nesting lists.

Creating a Matrix
Matrices are a structure that has rows and columns. To model a matrix in Python, we need a new list for each row, and we'll need to make sure that each list is the same length so that the columns work properly.

Here's an example matrix not in code:

1 2 3
4 5 6

To model this matrix in Python, we'll do this:

>>> my_matrix = [[1, 2, 3],
...              [4, 5, 6]]
>>> my_matrix
[[1, 2, 3], [4, 5, 6]]

To determine how many rows are in a multi-dimensional list, we need to use the len function on the matrix itself. To get the number of columns, we would use len on any row in the matrix (assuming that it's a proper matrix with each row having the same number of columns):

>>> row_count = len(my_matrix)
>>> column_count = len(my_matrix[0])
>>> row_count
2
>>> column_count
3

Now if we want to interact with an individual item in the matrix, we need to index our variable two times, first with the row, and second with the column:

>>> my_matrix[0][1]
2

Squares and Cubes
Matrixes with specific dimensions have names. If a matrix has the same number of rows as columns, then it can be classified as a "cube", and some cubes have unique names. A square is 2x2, and a cube (like the 3D shape) is 3x3. The matrix that we've already created is a 2x3 matrix, and this doesn't have a special name.
