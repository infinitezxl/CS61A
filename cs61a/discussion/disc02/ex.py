def keep_ints_recur (cond ,n):
    """Print out all intergers 1..i..n where cond(i) is true 

    >>> def is_even(x):
    ...    # Even number have remainder 0 when divided by 2.
    ...    return x%2==0
    >>> keep_ints_recur(is_even,5)
    2
    4
    """
    if not n==1:
        keep_ints_recur(cond ,n-1)
    if cond(n):
        print (n)
def keep_ints_iter(cond ,n):
    """Print out all intergers 1..i..n where cond(i) is true

    >>> def is_even(x):
    ...     # Even number have remainder 0 when divided by 2.
    ...     return x%2==0
    >>> keep_ints_iter(is_even ,5)
    2
    4
    """
    i=1
    while i<n:
        if cond(i):
            print(i)
        i=i+1
def keep_ints_curry_recur(n):
    """return a function which takes one parameter cond and prints out all integ    er 1..i..n where calling cond(i) return True.
    
    >>> def is_even(x):
    ...    # Even numbers have remainder 0 when divided by 2.
    ...    return x%2==0
    >>> keep_ints_curry_recur(5)(is_even)
    2
    4
    """
    def inner(cond):
        if not n==1:
            keep_ints_curry_recur(n-1)(cond)
        if cond(n):
            print(n)
    return inner

def keep_ints_curry_iter(n):
    """return a function which takes one parameter cond and prints out all integ    er 1..i..n where calling cond(i) return True.
    
    >>> def is_even(x):
    ...    # Even numbers have remainder 0 when divided by 2.
    ...    return x%2==0
    >>> keep_ints_curry_recur(5)(is_even)
    2
    4
    """
    def take_cond(cond):
        i=0
        while i<n:
            if cond(i):
                print(i)
            i+=1
    return take_cond

def multiply(m,n):
    """
    >>> multiply(5,3)
    15
    """
    if n==0:
        return 0
    return multiply(m,n-1)+m

def countdown(n):
    """

    >>> countdown(3)
    3
    2
    1
    """
    print(n)
    if not n==1:
        countdown(n-1)

def countup(n):
    """

    >>> countup(3)
    1
    2
    3
    """
    if not n==1:
        countup(n-1)
    print(n)

def sum_every_other_digit(n):
    """

    >>> sum_every_other_digit(7)
    7
    >>> sum_every_other_digit(30)
    0
    >>> sum_every_other_digit(228)
    10
    >>> sum_every_other_digit(123456)
    12
    >>> sum_every_other_digit(1234567)
    16
    """
    def spilt(n):
        return n%10,n//100
    last,droped_two=spilt(n)
    if n==0:
        return 0
    else:
        return last+sum_every_other_digit(droped_two)
