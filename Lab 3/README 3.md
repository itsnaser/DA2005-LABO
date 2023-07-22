# Task 3 - Iteration, file handling, error handling, and dictionaries

## Introduction 

This lab contains several independent tasks involving important basic algorithms, dictionaries, file handling, and error handling.

## Tasks 

### 3.3.1 Task 1: Insertion sort (2 points)

Insertion sort is a common sorting algorithm, that is, a method for sorting the elements of a list. The idea in this algorithm is similar to one way of sorting a deck of cards: take cardsq from the original deck one at a time and add each card to a new sorted deck of cards in the correct position.

We can divide up the insertion sort algorithm into two subproblems:

1. Write a function that inserts an element x in an already sorted list sorted_list in an appropriate position so that the list remains sorted:

```
def insert_in_sorted(x,sorted_list):
# here be code
```

#### Algorithm idea
- Assume that sorted_list is sorted.
- Iterate over all indices i < len(sorted_list) until you find an element sorted_list[i] such that sorted_list[i] > x and insert x before that element.
- If there is no sorted_list[i] that is larger than x, then insert x at the end of the list.

Sample tests:

```
>>> insert_in_sorted(2,[])
[2]

>>> insert_in_sorted(5,[0,1,3,4])
[0, 1, 3, 4, 5]

>>> insert_in_sorted(2,[0,1,2,3,4])
[0, 1, 2, 2, 3, 4]

>>> insert_in_sorted(2,[2,2])
[2, 2, 2]
```
2. Write insertion sort with the help of insert_in_sorted:

```
def insertion_sort(my_list):
# here be code
```

#### Algorithm idea
- Initialize a variable out with an empty list.
- For each element x in my_list, insert it in out with the help of insert_in_sorted.
- Return out.

Sample tests:

```
>>> insertion_sort([12,4,3,-1])
[-1, 3, 4, 12]

>>> insertion_sort([])
[]
```

### 3.3.2 Task 2: sparse matrices (1 point)

We can represent a matrix in Python as a list whose elements are lists of numbers all of the same length. For example, the matrix:
```
[1   0   0   2]
[0   8   0   0]
[0   0   0   5]
```

can be represented as [[1, 0, 0, 2], [0, 8, 0, 0], [0, 0, 0, 5]].

A matrix is called sparse if most of its entries are 0. If we represent such a matrix as a list of lists, we could unnecessarily use up a lot of the computer’s memory, especially if the matrix is very big—imagine a matrix with many millions of rows and columns that only contains a handful of elements that are not 0.
A better way of representing matrices like this is as a dictionary from coordinates to non-zero elements.

If the coordinates are of the form (row, column) and we begin counting from zero, then the matrix above can be written in the following way as a dictionary:

`{(0, 0): 1, (0, 3): 2, (1, 1): 8, (2, 3): 5}`

Write a function `matrix_to_sparse` that takes in a matrix represented as a list of lists and produces a dictionary as above. You can assume that the matrix is well-formed (that is, all the lists inside it have the same length).

Sample tests:

```
>>> matrix_to_sparse([[1,0,0,2],[0,8,0,0],[0,0,0,5]])
{(0, 0): 1, (0, 3): 2, (1, 1): 8, (2, 3): 5}

>>> matrix_to_sparse([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
{}

>>> matrix_to_sparse([[0,0],[0,0],[0,0],[0,10]])
{(3, 1): 10}
```

### 3.3.3 Task 3: file handling (1 point)

Write a function `annotate(f)` that takes a filename f as a parameter and writes to a new file annotated_f so that each line in annotated_f contains the original line in f followed by the row number (counting from 0) and total number of words up to and including that row.

**Example:** if the file infile.txt contains:

> A Dead Statesman
>
> I could not dig; I dared not rob:\
> Therefore I lied to please the mob.\
> Now all my lies are proved untrue\
> And I must face the men I slew.\
> What tale shall serve me here among\
> Mine angry and defrauded young?

then running annotate('infile.txt') should produce a file annotated_infile.txt that contains:

```

A Dead Statesman 0 3
13
 1 3
I could not dig; I dared not rob: 2 11
Therefore I lied to please the mob. 3 18
Now all my lies are proved untrue 4 25
And I must face the men I slew. 5 33
What tale shall serve me here among 6 40
Mine angry and defrauded young? 7 45
```

### 3.3.4 Task 4: searching for strings in files (2 points)

1. Write a function `find_matching_lines(h,s)` that takes a file handle h and a string s. The function should return, in the form of a list of tuples, both the row number (counting from 0) and the contents of each row that contains the string.

#### Example (with infile.txt as above):

```
>>> hinfile = open('infile.txt')

>>> find_matching_lines(hinfile, 'the mob')
[(3, 'Therefore I lied to please the mob.\n')]

>>> hinfile.close()

>>> hinfile = open('infile.txt')

>>> find_matching_lines(hinfile, 'the')
[(3, 'Therefore I lied to please the mob.\n'), (5, 'And I must face the men I slew.\n')]

>>> hinfile.close()

>>> with open('infile.txt') as h:
... print(find_matching_lines(h, 'sommar'))
[]
```

**Obs:** your search should be case sensitive, that is, “the” should not be considered the same as “The”.

**Obs:** `find_matching_lines` should take a file handle, so it should not contain any call to open but rather should assume that open was called before the function itself was called, as in the tests above.

2. Write a function `find_lines()` that asks the user for a file and string and uses the function `find_matching_lines` to print out the rows where the string was found.

**Example:** an execution of find_lines(), with infile.txt as above, could appear as follows:

```
Hello, which file do you want to search in? infile.txt
Ok, searching in "infile.txt".

What do you want to search for? the
The result after searching for "the" is:

Line 3: Therefore I lied to please the mob.
Line 5: And I must face the men I slew.
```

If is up to you whether the program continues to ask repeatedly for input and whether the user can change the file to search in, etc. As long as the user can choose the file and string and you use `find_matching_lines` in your code, you will get credit.

### 3.3.5 Task 5: searching by position in files (4 points)

1. Write a function `save_rows(h)` that takes a file handle h and saves the line numbers as keys and lines themselves as values in a dictionary. The function should return the dictionary.

**Example:** if the input file infile2.txt contains:

> Hey you\
> the moon revolves around earth\
> two chairs and the table

then the following should return a dictionary as shown:

```
>>> with open('infile2.txt') as hinfile:
... print(save_rows(hinfile))
{0: 'Hey you', 1: 'the moon revolves around earth', 2: 'two chairs and the table'}
```

**Obs:** note that there are no \ns at the end of the strings in the output.

2. Write a function lookup that takes in a dictionary d from numbers to strings as above as well as two coordinates (r,c) which correspond to a row and column in d and returns the character at the position corresponding to the coordinates.

The idea is that lookup will be used together with `save_rows` (see part 3)) and each character in the file can be said to be at a certain row and column. For example, the word “Hey” in infile2.txt occupies the three coordinates (0,0), (0,1), (0,2). In the same way, the word “chairs” takes up the coordinates (2,4), (2,5), . . . , (2,9).

We assume a 0-indexed coordinate system (as is usual in programming).

The following cases should be handled specially:
- If the row and/or column does not exist in d, then the program should raise a `LookupError`.
- If the position is a space, then the string “Space” should be returned.

Sample tests:

```
>>> with open('infile2.txt') as hinfile2:
... d = save_rows(hinfile2)
... print(lookup(d,0,0))
... print(lookup(d,2,9))
... print(lookup(d,2,10))
H
s
Space
```

But if one calls for example `lookup(d,3,0)` or `lookup(d,0,7)`, then the function should raise a `LookupError`.

3. Use save_rows and lookup to write a code snippet (a “program”) that
    - Asks the user for a file and reads in the file to a dictionary (using save_rows)
    - Asks the user to give coordinates for a row number and column number.
    - Uses lookup to fetch and then write out the character in the file at that coordinate.

The user should be able to give several coordinates until they choose to write exit, whereupon the program should exit. You can decide how to structure your code snippet yourself; for example, you can define a function `main()` that takes no parameters but contains code as described in 1-3 above:

```
def save_rows(...):
...

def lookup(...):
...

def main():
    infile2 = input('Ange en fil: ')
    indexed_file = save_rows(...)
    # More code here for steps 2 and 3
```

If lookup raises an exception because the coordinates are outside the text, then it should be caught with try-except. Then the program should print the message Warning: Out of bounds, try again! and continue to execute.

Example: if the user runs the program with the file infile2.txt as above, then an execution of the program should look like so:

```
At any point type "exit" to quit.

Provide row: 0
Provide column: 3

Space

Provide row: 1
Provide column: 1

h

Provide row: 3
Provide column: 1

Warning: Out of bounds, try again!

Provide row: 2
Provide column: 9

s

Provide row: exit
```