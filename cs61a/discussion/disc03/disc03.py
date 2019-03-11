def is_prime(n):
    """

    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
    """
    def prime_helper(n,m=n):
        if n==1:
            return 1
        elif m%n==0:
            return prime_helper(n-1,m)+1
        else:
            return prime_helper(n-1,m)
    return prime_helper(n)==2
def make_func_repeater(f,x):
    """

    >>> incr_1=make_func_repeater(lambda x:x+1,1)
    >>> incr_1(2) #same as f(f(x))
    3
    >>> incr_1(5)
    6
    """

    def repeat(n):
        if n==1:
            return f(x)
        else:
            return f(f(n-1))
    return repeat
def count_stair_ways(n):
    """
    >>> count_stair_ways(1)
    1
    >>> count_stair_ways(2)
    2
    >>> count_stair_ways(3)
    3
    """
    if n<0:
        return 0
    elif n==0:
        return 1
    else:
        return count_stair_ways(n-1)+count_stair_ways(n-2)

def count_k(n,k):
    """

    >>> count_k(3,3) # 3,2+1,1+2,1+1+1
    4
    >>> count_k(4,4)
    8
    >>> count_k(10,3)
    274
    >>> count_k(300,1) #only one step at a time
    1
    """
    if n<0:
        return 0
    elif n==0:
        return 1
    else:
        total,i=0,k
        while i:
            total=total+count_k(n-i,k)
            i-=1
    return total

def count_k(n,k):
    """
    >>> count_k(3,3) # 3,2+1,1+2,1+1+1
    4
    >>> count_k(4,4)
    8
    >>> count_k(10,3)
    274
    >>> count_k(300,1) #only one step at a time
    1
    """
    if n<0:
        return 0
    elif n==0:
        return 1
    else:
        total,i=0,k
        while i:
            total+=count_k(n-i,k)
            i-=1
    return total
    
def pascal(row,column):
    if column==0:
        return 1
    elif row==column:
        return 1
    elif row<column:
        return 0
    else:
        return pascal(row-1,column)+pascal(row-1,column-1)
