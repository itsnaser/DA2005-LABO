# Task 2 - Polynomials

## Introduction

In this lab, we will represent polynomials using lists of coefficients. The word “representation” here
means approximately “way of storing in a computer”. Concretely, we will represent a polynomial like
`1 + 3x + 7xˆ2` in Python as the list `[1,3,7]`. In general, we will store the coefficient of degree n in the list’s
nth entry

In this lab, we will represent polynomials as lists. Below are some more examples:
| Polynomial                 | Python representation  |
| -------------------------- | ---------------------- |
| x^4                        | [0, 0, 0, 0, 1]        |
| 4x^2 + 5x^3                | [0, 0, 4, 5]           |
| 5 + 4x + 3x^2 + 2x^3 + x^4 | [5, 4, 3, 2, 1]        |

Obs: you can assume that the lists you work with only contain numbers.


The Python file `polynom.py` contains a function, `poly_to_string`, which converts a polynomial represented by a list to a string.

To get started with the lab, create a file labb2.py and copy over the function `poly_to_string`. Complete the tasks below by adding the necessary code to solve the specified problems. As you will see, you will also need to modify the function `poly_to_string` (see task 2).

Obs: you may not use functions from any library in the lab, i.e. you should not use the “import” keyword
anywhere in your solution.

## Tasks 

### Task 1 (0 points, but necessary for tests later in lab)

Suppose that the polynomials p and q are defined as below.

```
p := 2 + x^2`
q := −2 + x + x^4
```

Write Python code to store list representations for these two polynomials in the variables p and q. That is, write

```
p = [...]
q = [...]
```

with the contents of the lists filled in. Check that you encoded the polynomials correctly using
`poly_to_string`. You should get the following:

```
>>> poly_to_string(p)
'2 + 0x + 1x^2'
```
```
>>> poly_to_string(q) 
'-2 + 1x + 0x^2 + 0x^3 + 1x^4'
```


Here, we write >>> for the “prompt” of the Python interpreter: poly_to_string(p) is a command that
should be run by Python, and the lines after are the results. The prompt may look different depending
on your computer and interpreter. You can also check the results by adding

`print(poly_to_string(p))`

to your file and running it, then observing what is printed in the console. In this case you should not see
`2 + 0x + 1xˆ2` but rather `2 + 0x + 1xˆ2` (without surrounding quote marks). This type of test is
very useful when developing code, but you should make sure to remove any print calls used for testing
in the final code you hand in. It can however be good to add comments with tests and expected results
to make it easy for someone reading your code to go through and test it.

### Task 2 (3 points)

Edit the poly_to_string function so that:

- The empty list is converted to 0.
- Terms with coefficent 1 are written without a coefficient. For example, `1xˆ2` should instead be written `xˆ2`.
- Terms with coefficient -1 add a minus before the term, but the 1 is not written. For example `2 + -1xˆ2` should instead be `2 + -xˆ2`.
- Terms with coefficient 0 are not written. For example, `0 + 0x + 2xˆ2` should be simplified to 2xˆ2.
- A list that contains only 0s as elements, for example `[0, 0, 0]`, should be written as 0.

Here are some examples with the expected output:

```
>>> poly_to_string(p)
'2 + x^2'

>>> poly_to_string(q)
'-2 + x + x^4'

>>> poly_to_string([])
'0'

>>> poly_to_string([0,0,0])
'0'

>>> poly_to_string([1,2,3])
'1 + 2x + 3x^2'

>>> poly_to_string([-1, 2, -3])
'-1 + 2x + -3x^2'

>>> poly_to_string([1,1,-1])
'1 + x + -x^2'
```

### Task 3 (2 points)

1. Write a function drop_zeroes that removes all zeros at the end of a polynomial and returns the result.

```
def drop_zeroes(p_list):
    # here be code
```

Define some polynomials with zeroes at the end, for example:

```
p0 = [2,0,1,0] # 2 + x^2 + 0x^3
q0 = [0,0,0] # 0 + 0x + 0x2
```

and use these to test your function:

```
>>> drop_zeroes(p0)
[2, 0, 1]

>>> drop_zeroes(q0)
[]

>>> drop_zeroes([])
[]
```

2. Write a function that tests when two polynomials are equal by ignoring all zeroes at the end and then comparing the rest for equality:

```
def eq_poly(p_list,q_list):
# here be code
```

Example tests:

```
>>> eq_poly(p,p0)
True

>>> eq_poly(q,p0)
False

>>> eq_poly(q0,[])
True
```

Obs: The functions drop_zeroes and eq_poly should return their results, not just print them out. The
difference can be difficult to understand for a beginner, since the result may look the same when you run
the code, but there is a big difference between a function that returns something and one that just prints
something.
Note that the code you were given for poly_to_string returned the result as a string. Does your
solution to Task 2 look similar? If not, go back and make sure you are returning.

### Task 4 (2 points)

Write a function named `eval_poly` that takes a polynomial and a value in a variable x and returns the
polynomials value at the point x.


- Iterate over the polynomial’s terms by iterating over the coefficients.
- Keep track of the degree of the current term and the sum of the values of the terms you have seen so far. In each step of the iteration, calculate the value of the term as coeff * x ** grade (recall that ** is exponentiation). Then add the term’s value to the sum.
- When you have finished interating, return the final sum.

Sample tests:

```
>>> eval_poly(p,0)
2

>>> eval_poly(p,1)
3

>>> eval_poly(p,2)
6

>>> eval_poly(q,2)
16

>>> eval_poly(q,-2)
12
```

### Task 5 (3 points)

1. Define negation of polynomials (that is, flip the sign of all coefficients and return the result).

```
def neg_poly(p_list):
# here be code
```

2. Define addition of polynomials (that is, add the coefficients and return the result).

```
def add_poly(p_list,q_list):
# here be code
```

3. Define subtraction of polynomials.

```
def sub_poly(p_list,q_list):
# here be code
```

Sample tests:

```
# p + q = q + p
>>> eq_poly(add_poly(p,q),add_poly(q,p))
True

# p - p = 0
>>> eq_poly(sub_poly(p,p),[])
True

# p - (- q) = p + q
>>> eq_poly(sub_poly(p,neg_poly(q)),add_poly(p,q))
True

# p + p != 0
>>> eq_poly(add_poly(p,p),[])
False

# p - q = 4 - x + x^2 - x^4
>>> eq_poly(sub_poly(p,q),[4, -1, 1, 0, -1])
True

# (p + q)(12) = p(12) + q(12)
>>> eval_poly(add_poly(p,q),12) == eval_poly(p,12) + eval_poly(q,12)
True
```
