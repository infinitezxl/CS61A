def longest_increasing_suffix(n):
    """Return the longest incressing suffix of a positive interger n.

    >>> longest_increasing_suffix(63134)
    134
    >>> longest_increasing_suffix(233)
    3
    >>> longest_increasing_suffix(5689)
    5689
    >>> longest_increasing_suffix(568901) # 01 is the suffix,display as 1
    1
    """
    m,suffix,k=10,0,1
    while n:
        n,last=n//10,n%10
        if m>last:
            m,suffix,k=last,suffix+k*last,10*k
        else:
            return suffix

    return suffix

def sandwich(n):
    """Return Ture if n contains sandwich and False otherwise

    >>> sandwich(416263) # 626
    True
    >>> sandwich(5050) # 505 ot 050
    True
    >>> sandwich(4441) # 444
    True
    >>> sandwich(1231)
    False
    >>> sandwich(55)
    False
    >>> sandwich(4456)
    False
    """
    
    tens,ones=n//10%10,n%10
    n=n//100
    while n:
        if ones==n%10:
            return True
        else:
            tens,ones=n%10,tens
            n=n//10
    return False
def luhn_sum(n):
    """Return the Luhn sum of n.

    >>> luhn_sum(135) # 1+6+5
    12
    >>> luhn_sum(185) # 1+(1+6)+5
    13
    >>> luhn_sum(138743) # From lecture: 2+3+(1+6)+7+8+3
    30
    """
    def luhn_digit(digit):
        x=digit*multiplier
        return (x//10)+x%10
    total,multiplier=0,1
    while n:
        n,last=n//10,n%10
        total=total+luhn_digit(last)
        multiplier=3-multiplier
    return total

def print_numbers(n,k):
    """Print all numbers that(A) can be formed from the digits of 'n' in reverse    order and (B) are multiples of 'k'.

    This is essentially Fall 2015 Midterm 2 #3c written to not depend on knowled    dge of lists.

    Args:
    n (int): The number that results must use digits from.
    k (int): The number that results nust be multiples of.

    >>> print_numbers(97531,5)
    135
    15
    35
    >>> print_numbers(97531,7)
    1379
    357
    35
    >>> print_numbers(97531,2)
    """
    def inner(n,s):
        if n==0:
            if s%k==0 and not s==0 and not s==k:
                print(s)
        else:
            inner(n//10,10*s+n%10)
            inner(n//10,s)
    return inner(n,0)

def sixty_ones(n):
    """Return the number of times that a 1 directly follows a 6 in the digits of    'n'.

    This is essentially Fall 2014 Midterm 2 #3a Written to not depend on knowled    ge of lists.

    Args:
        n(int):The number of time whose digits are to be examined

    Returns:
        int : The number of ocurrences

    >>> sixty_ones(461601)
    1
    >>> sixty_ones(161461601)
    2
    """
    if n==0:
        return 0
    elif n%100==61:
        return sixty_ones(n//10)+1
    else:
        return sixty_ones(n//10)

def no_elevens(n):
    """Return the number of 'n' -digit numbers whose digita consistof 1's and 6'    s and do not contain a'1' and then another '1' consicutively
    

    This is essentially Fall 2014 Midterm 2 #3b rewritten to not depend on knowl    edge of lists

    Args:
       n(int): The lengeh of the numbers

    Return:
        int: the number of numbers.
    >>> no_elevens(2)  # 66.61,16
    3
    >>> no_elevens(3)  # 666 661 616 166 161
    5
    """
    if n==0:
        return 1
    if n==1:
        return 2
    else:
        return no_elevens(n-1)+no_elevens(n-2)

def make_skipper(n):
    """

    >>> a=make_skipper(2)
    >>> a(5)
    1
    3
    5
    """
    def inner(x):
        if not x==0:
            inner(x-1)
        if not x%n==0:
            print(x)
    return inner

def make_alternator(f,g):
    """

    >>> a=make_alternator(lambda x:x*x,lambda x:x+4)
    >>> a(5)
    1
    6
    9
    8
    25
    >>> b=make_alternator(lambda x:x*2,lambda x:x+2)
    >>> b(4)
    2
    4
    6
    6
    """
    def helper(x):
        def inner(i):
            if i<=x:
                if i%2==1:
                    print(f(i))
                else:
                    print(g(i))
            else:
                return None
            return inner(i+1)
        return inner(1)
    return helper

def mario_number(level):
    """
    Return the number of ways that Mario can traverse the level ,where Mario can    either hop by one digit or two digits each turn.
    A level is defined as being an integer with digits where a 1 is something Ma    rio can step on and 0 is something Mario cannot step on.

    >>> mario_number(10101) # Hops each turn (1,2,2)
    1
    >>> mario_number(11101) # Hops each turn (1,1,1,2),(2,1,2)
    2
    >>> mario_number(100101) # No way to traverse through level
    0
    """
    if level==0 :
        return 1
    elif level%100==0:
        return 0
    elif level%100==10:
        return mario_number(level//100)
    elif level%100==1:
        return mario_number(level//10)
    else:
        return mario_number(level//10)+mario_number(level//100)
            

def mario_number(level):
    """
    Return the number of ways that Mario can traverse the level,
    where Mario can either hop by one digit or two digits each turn.
    A level is defined as being an integer with digits where a 1 is
    something Mario can step on and 0 is something Mario cannot step
    on.
    >>> mario_number(10101) # Hops each turn: (1, 2, 2)
    1
    >>> mario_number(11101) # Hops each turn: (1, 1, 1, 2), (2, 1, 2)
    2
    >>> mario_number(100101)# No way to traverse through level
    0
    """
    if level==1:
        return 1
    elif level%10==0:
        return 0
    else:
        return mario_number(level//10)+mario_number(level//100)

from operator import add ,mul

def combine(n,f,result):
    """
    combine the digits in n using f.
    >>> combine(3,mul,2) # mul (3,2)
    6
    >>> combine(43,mul,2) # mul(4,mul(3,2))
    24
    >>> combine(6502,add,3) # add (6,add(5,add(0,add(2,3)))
    16
    >>> combine(239,pow,0) # pow(2,pow(3,pow(9,0)))
    8
    """
    if n==0:
        return result
    else:
        return combine(n//10,f,f(n%10,result))
