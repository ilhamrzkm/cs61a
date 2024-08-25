def is_prime(n):
    """
    One sentence description:
    This function is only to return True by recursively checking n modulo i != 0 from i up to n.
    
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number
    False
    """

    i = 2

    if n < 2:
        return False
    
    while i < n:
        if n % i == 0:
            return False
        elif n % i != 0:
            i = i + 1
    return True