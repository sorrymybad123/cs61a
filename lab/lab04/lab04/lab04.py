HW_SOURCE_FILE = __file__


def summation(n, term):
    """Return the sum of numbers 1 through n (including n) wíth term applied to each number.
    Implement using recursion!

    >>> summation(5, lambda x: x * x * x) # 1^3 + 2^3 + 3^3 + 4^3 + 5^3
    225
    >>> summation(9, lambda x: x + 1) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    54
    >>> summation(5, lambda x: 2**x) # 2^1 + 2^2 + 2^3 + 2^4 + 2^5
    62
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'summation',
    ...       ['While', 'For'])
    True
    """
    assert n >= 1
    "*** YOUR CODE HERE ***"
    return summation_help(n, term, 0)


def summation_help(n, term, total):
    if n <= 0:
        return total 
    else:
        total += term(n) 
        return summation_help(n - 1, term, total)
    
def pascal(row, column):
    """Returns the value of the item in Pascal's Triangle
    whose position is specified by row and column.
    >>> pascal(0, 0)    # The top left (the point of the triangle)
    1
    >>> pascal(0, 5)	# Empty entry; outside of Pascal's Triangle
    0
    >>> pascal(3, 2)	# Row 3 (1 3 3 1), Column 2
    3
    >>> pascal(4, 2)     # Row 4 (1 4 6 4 1), Column 2
    6
    """
    "*** YOUR CODE HERE ***"
    return pascal_help(row, column)

""" 打印出[[1], [1,1], [1,2,1], [1,3,3,1], [1, 4, 6, 4, 1]]

1(0, 0)
1(1, 0) 1(1, 1)
1(2, 0) 2(2, 1) 1(2, 2)
1(3, 0) 3(3, 1) 3(3, 2) 1(3, 3)

"""



def pascal_help(row, column):
    if row < 0:
        return 0
    elif column < 0:
        return 0
    elif column > 2 ** (row) - 1:
        return 0
    if row == 0 and column == 0:
        return 1
     

    else:

        return pascal_help(row - 1, column - 1) + pascal_help(row - 1, column) 
    
    
     

def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    if m == 1 and n == 1:

        return 1
    elif m < 1 or n < 1:

        return 0

    else:
              
        return paths(m - 1, n) + paths(m, n - 1) 

def couple(s, t):
    """Return a list of two-element lists in which the i-th element is [s[i], t[i]].

    >>> a = [1, 2, 3]
    >>> b = [4, 5, 6]
    >>> couple(a, b)
    [[1, 4], [2, 5], [3, 6]]
    >>> c = ['c', 6]
    >>> d = ['s', '1']
    >>> couple(c, d)
    [['c', 's'], [6, '1']]
    """
    assert len(s) == len(t)
    "*** YOUR CODE HERE ***"
    result = [] 
    for i in range(len(s)):
        result.append([s[i]] + [t[i]])
    return result


def double_eights(n):
    """ Returns whether or not n has two digits in row that
    are the number 8. Assume n has at least two digits in it.

    >>> double_eights(1288)
    True
    >>> double_eights(880)
    True
    >>> double_eights(538835)
    True
    >>> double_eights(284682)
    False
    >>> double_eights(588138)
    True
    >>> double_eights(78)
    False
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'double_eights', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n <= 0:
        return False
    elif n % 100 == 88:
        return True
    else:
        return double_eights(n // 10) 


def coords(fn, seq, lower, upper):
    """
    >>> seq = [-4, -2, 0, 1, 3]
    >>> fn = lambda x: x**2
    >>> coords(fn, seq, 1, 9)
    [[-2, 4], [1, 1], [3, 9]]
    """
    "*** YOUR CODE HERE ***"
    result = []
    for i in seq:
        y = fn(i) 
        if y <= upper and y >= lower:
            result.append([i]+[y])

    return result 


def riffle(deck):
    """Produces a single, perfect riffle shuffle of DECK, consisting of
    DECK[0], DECK[M], DECK[1], DECK[M+1], ... where M is position of the
    second half of the deck.  Assume that len(DECK) is even.
    >>> riffle([3, 4, 5, 6])
    [3, 5, 4, 6]
    >>> riffle(range(20))
    [0, 10, 1, 11, 2, 12, 3, 13, 4, 14, 5, 15, 6, 16, 7, 17, 8, 18, 9, 19]
    """
    "*** YOUR CODE HERE ***"
    result = []
    middle = len(deck) // 2
    front = 0
    for i in range(len(deck)):
        if i % 2 == 0:
            result.append(deck[front])
            front += 1 
        elif i % 2 == 1:
           
            result.append(deck[middle])
            middle += 1
            
    return result 
