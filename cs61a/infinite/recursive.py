def is_prime(n):
    def prime_helper(num_factor,factor):
        if factor==n+1:
            return num_factor==2
        elif n%factor==0:
            num_factor+=1
            return prime_helper(num_factor,factor+1)
        else:
            return prime_helper(num_factor,factor+1)
    return prime_helper(0,1)

