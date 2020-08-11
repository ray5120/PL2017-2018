#Jamie's coursework template

#Name: Wang Wu (Raymond), , User ID: WCW3 My Regno:H00262859   <--- so we know who you are 
#F28PL Coursework PY1                         <--- sanity check


# You may assume variables, procedures, and functions defined in earlier questions
# in your answers to later questions, though you should add comments in code explaining
# this if any clarification might help read your code.


################################################################################
# Question 1   <--- Yes, so we know what question you think you're answering
print()
print('Question 1')

"""
The complex numbers are explained here (and elsewhere):
 http://www.mathsisfun.com/algebra/complex-number-multiply.html
Represent a complex integer as a pair of integers, so (4,5) represents 4+5i (or 4+5j,
depending on the complex numbers notation you use).
1a. Using def, define functions cadd and cmult representing complex integer addition and
multiplication.
For instance,
 cadd((1,0),(0,1))
should compute
 (1,1).
1b. Python has its own native implementation of complex numbers. Write translation functions
tocomplex and fromcomplex that map (x1,y1) to x1+(y1)j and vice versa. You may use the
python methods real and imag without comment, but not complex (use j directly instead).
"""


#  <--- always have the question under your nose

#####################################
# Question 1a
def cadd(a, b):
    a = complex(a[0], a[1])
    b = complex(b[0], b[1])
    result = a + b
    return (result.real, result.imag)


def cmult(a, b):
    a = complex(a[0], a[1])
    b = complex(b[0], b[1])
    result = a * b
    return (result.real, result.imag)


# print('input data as: 1,1')
# input_a = input('a: ').split(',')
# a = (int(input_a[0]), int(input_a[1]))
# input_b = input('b: ').split(',')
# b = (int(input_b[0]), int(input_b[1]))
a = (1, 0)
b = (0, 1)
print('input data: %s %s' % (a, b))
print('Cadd')
print(cadd(a, b))
print('\nCmult')
print(cmult(a, b))


#####################################
# Question 1b
def fromcomplex(x1, y1):
    result = complex(x1, y1)
    return result


def tocomplex(x):
    complex_numb = complex(x)
    real = complex_numb.real
    imag = complex_numb.imag
    return real, imag


# x1 = int(input('x1:'))
x1 = 4
# y1 = int(input('y1:'))
y1 = 7
print('\ninput data: x1=%s y1=%s' % (x1, y1))
# img = input('input complex number(example: 3+4j): ')
img = 3 + 4j
print('from complex:', fromcomplex(x1, y1))
print('input complex number: %s' % img)
print('to complex: ', tocomplex(img))
# END ANSWER TO Question 1
################################################################################



################################################################################
# Question 2
print()
print('Question 2')

"""
2a. Using def, write iterative functions seqaddi and seqmulti that implement pointwise
addition and multiplication of integer sequences.
For instance
 seqaddi([1,2,3],[~1,2,2])
should compute
 [0,4,5]
You need not write error-handling code to handle the cases that sequences have different
lengths.
2b. Do as for 2a, but make your functions recursive (as for ML).
Call them seqaddr and seqmultr.
2c. Do it again. This time use list comprehensions instead of iteration or recursion.
"""


#####################################
# Question 2a
def seqaddi(arr1, arr2):
    result = []
    for a, b in zip(arr1, arr2):
        result.append(a+b)
    return result


def seqmulti(arr1, arr2):
    result = []
    for a, b in zip(arr1, arr2):
        result.append(a * b)
    return result


#####################################
# Question 2b
def recursive_sum(l1, l2, result = None, idx = 0):
    if result is None:
        result = []
    if idx < min(len(l1), len(l2)):
        result.append(l1[idx] + l2[idx])
        return recursive_sum(l1, l2, result, idx + 1)
    else:
        return result
#####################################
# Question 2c
def comprehension_sum(arr1, arr2):
    result = [a + b for a, b in zip(arr1, arr2)]
    return result
arr1 = [1,2,3]
arr2 = [4,5,6]
print('input data %s %s' % (arr1, arr2))
print('seqaddi: ', seqaddi(arr1, arr2))
print('seqmulti: ', seqmulti(arr1, arr2))
print('recursive_sum: ', recursive_sum(arr1, arr2))
print('comprehension_sum', comprehension_sum(arr1, arr2))

# END ANSWER TO Question 2
################################################################################




################################################################################
# Question 3
print()
print('Question 3')

"""
Write functions
● ismatrix
This should input a list of list of integers (henceforth an intmatrix) and test whether a list
of lists of integers represents a matrix (so the length of each row should be equal).
● matrixshape
This should input an intmatrix and return a pair that is the number of columns, and the
number of elements in any row.
● matrixadd
Matrix addition, which is simply pointwise addition.
● matrixmult
Similarly for matrix multiplication.
You do not need to write error-handling code, e.g. for the cases that inputs do not represent
matrices or represent matrixes of the wrong shapes; so for instance your matrixshape may
assume that the argument has successfully passed the test ismatrix.
Your answer can use iteration, recursion, list comprehension, or anonymous functions. You
should not appeal to any libraries, e.g. for matrix processing.  Don't use zip.
"""
m1 = [[1, 2], [3, 4]]
m2 = [[5, 6], [7, 8]]

def ismatrix(matrix):
    n1 = len(matrix[0])
    for line in matrix:
        nn = len(line)
        if n1 != nn:
            print('Non matrix')
            return
    print('Is matrix')
    return '%s is matrix' % matrix


def matrixshape(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    return cols, rows


def matrixadd(m1, m2):
    res = []
    for i in range(len(m1)):
        row = []
        for j in range(len(m1[0])):
            row.append(m1[i][j] + m2[i][j])
        res.append(row)
    return res


def matrixmult(m1, m2):
    result = [[0 for y in range(len(m2[0]))] for x in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m1)):
            for k in range(len(m1[0])):
                result[i][j] = m1[i][k] * m2[k][j]
    return result

print('input data: \nm1: %s\nm2: %s' % (m1, m2))
print('ismatrix: %s' % ismatrix(m1))
print('matrixshape: cols=%s, rows=%s' % matrixshape(m1))
print('matrixadd: %s' % matrixadd(m1, m2))
print('matrixmult: %s' % matrixmult(m1, m2))
# END ANSWER TO Question 3
################################################################################



###############################################################################
# Question 4
print()
print('Question 4')

"""
Write an essay on Python data representation. Be clear, to-the-point, and concise. Convince
your marker that you understand:
● Mutable vs immutable types. Give at least two examples of each, with explanation.
● Integer vs float types.
● Assignment = vs equality == vs identity is.
● The computational effects of a call to list on an element of range type, as in
list(range(5**5**5)).
● Slices, with examples. Including an explanation of the difference in execution between
 list(range(10**10)[10:10]) and
 list(range(10**10))[10:10]
Include short code-fragments where appropriate (as I do when lecturing) to illustrate your
observations.
"""
explain1 = """
# The mutable object can change its state or contents and immutable objects cannot.
# Mutable objects:
# list, dict, set, byte array
l = [1, 2, 3]  # list
d = {'a': 1, 'b': 2}  # dict
# Immutable objects:
# int, float, complex, string, tuple, frozen set [note: immutable version of set], bytes
t = (1, 2, 3)  # tuple
i = 4  # int

# int (signed integers) − They are often called just integers or ints, are positive
#  or negative whole numbers with no decimal poin
x = 5
# float (floating point real values) − Also called floats, they represent real numbers
#  and are written with a decimal point dividing the integer and fractional parts.
#  Floats may also be in scientific notation, with E or e indicating the power of 10 (2.5e2 = 2.5 x 102 = 250).
f = 7.8

#You use = to assign values to symbols (variables, arrays, objects)
# a = 10 # the value of a is 10.
# You use == to compare two symbols or values and see if they are equal
# b = 5
# c = 10
# d = 10
# b == c #false because 5 is not equal to 10
# c == d #true because 10 is equal to 10

#List comprehensions provide a concise way to create lists.
#It consists of brackets containing an expression followed by a for clause, then
#zero or more for or if clauses. The expressions can be anything, meaning you can
#put in all kinds of objects in lists.
#The result will be a new list resulting from evaluating the expression in the
#context of the for and if clauses which follow it.
#The list comprehension always returns a result list.
# list(range(5**5**5)) => [......]


# list(range(10**10))[10:10] == []
# list(range(10**10)[10:10]) == []
# In two case we get empty list"""
print(explain1)

# END ANSWER TO Question 4
################################################################################



###############################################################################
# Question 5
print()
print('Question 5')

"""
Write a general encoding function encdat that will intput an integer, float, complex number, or
string, and return it as a string.

So
• encdat(-5) should return '-5'
• encdat(5.0) should return '5.0'
• encdat(5+5j) should return '5+5j'
• encdat('5') should return '5'

In formulating your answer, you may find it useful to consider the following code fragment
   type(5) == type('5')
"""


def encdat(input_data):
    return str(input_data)


print(encdat(-5))
print(encdat(5.0))
print(encdat(5 + 5j))
print(encdat('5'))

# END ANSWER TO Question 5
################################################################################


###############################################################################
# Question 6
print()
print('Question 6')

"""
An encoding f of numbers in lists is as follows:
• f(0) = [] (0 maps to the empty list)
• f(n+1) = [f(n),[f(n)]] (n+1 maps to the list that contains f(n) and singleton f(n))
Implement encode and decode functions in Python, that map correctly between nonnegative
integers and this representation. Call them fenc and fdec.
"""


def func(a):
    if not a:
        return []
    elif ',' in a:
        result = a.split(',')
    elif ' ' in a:
        result = a.split(' ')
    return result


print('input data: "1 2 3 4"')
print(func("1 2 3 4"))

# END ANSWER TO Question 6
###############################################################################


###############################################################################
# Question 7
print()
print('Question 7')

"""
Implement an iterator cycleoflife such that if we assign
 x = cycleoflife()
then repeated calls to
 next(x)
return the values
 eat
 sleep
 code
 eat
 sleep
 code
 ...
in an endless cycle. If you can’t manage an endless cycle, do a program that runs for 1000
cycles then stops.
Note that this question is not asking you to program an endless loop that prints these values.
In effect, I am asking you to implement what is called a stream (infinite list)
 x = [eat, sleep, code, eat, sleep, code, ...].
This does not mean the whole infinite datastructure is in memory at one time (which is
impossible for a machine with finite memory), but for any finite but unbounded number of calls
to next your generator behaves as if it were the infinite datastructure illustrated above.
"""


def cycleoflife():
    while True:
        yield 'eat'
        yield 'code'
        yield 'sleep'


x = cycleoflife()
for i in range(10):
    print(next(x))

# END ANSWER TO Question 7
################################################################################


#################################################################################
# Question 8
print()
print('Question 8')
"""
Call a *datum* something that is either an integer, or a list of data (datums).

Write a flatten function flatten that converts a datum to a list of integers.

So
- gendat(5) should return [5]
- gendat([])should return []
- gendat([5,[5,[]],[],[5]]) should return [5,5,5]

In formulating your answer, you may find it useful to consider the following code fragment
   type(5) == type([])
"""


def gendat(S):
    if type(S) == int:
        return [S]
    if S == []:
        return S
    if isinstance(S[0], list):
        return gendat(S[0]) + gendat(S[1:])
    return S[:1] + gendat(S[1:])
print('input gendat(5) => result %s' % gendat(5))
print('input gendat([]) => result %s' % gendat([]))
print('input gendat([5,[5,[]],[],[5]]) => result %s' % gendat([5,[5,[]],[],[5]]))
# END ANSWER TO Question 8
################################################################################




##########################################################
# Question 9
print()
print('Question 9')
"""
Implement the Sieve of Eratosthenes
 https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
as a Python generator eratosthenes such that if we assign
 x = eratosthenes()
then repeated calls to
 next(x)
return the primes, starting from 2.
"""


# not a endless generator this will only get primes upto the passed input or 40000
def eratosthenes(z=40000):
    # create an array of true values the size of z
    A = [True] * z
    # iterate over each value to z squared
    for x in range(2, int(z ** 0.5)):
        # if A[x] has a true value
        if A[x]:
            # iterate over a range starting from x*2 ending at z in jumps of x
            for z in range(x * 2, z, x):
                # set anything in the range to false
                A[z] = False
    # iterate over the array
    for y in range(2, len(A)):
        # if a value is true that index is a prime number
        if A[y]:
            # yield the current iterator location as it is a prime
            yield y


# creates a instance of the generator and prints out 50 primes
pNumbers = eratosthenes()
for printer2 in range(50):
    print(next(pNumbers))



    # END ANSWER TO Question 9
    ################################################################################
