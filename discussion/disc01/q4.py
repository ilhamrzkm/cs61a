def unique_digits(n):
    """
    Return the number of unique digits in a positive integer

    >>> unique_digits(8675309)
    7
    >>> unique_digits(13173171)
    3
    >>> unique_digits(101)
    2
    """
    
    unique = 0
    while n > 0:
        last = n % 10
        n = n // 10
        # Calls the has_digit() function if has digit return false counter + 1
        if not has_digit(n, last):
            unique += 1

    return unique


def has_digit(n, k):
    """
    Returns whether k is a digit in n.

    >>> has_digit(10,1)
    True
    >>> has_digit(12,7)
    False
    """
    assert k >= 0 and k < 10
    
    counter = False
    while n > 0:
        if n % 10 == k:
            counter = True
            n = n // 10
        else:
            n = n // 10

    
    return counter