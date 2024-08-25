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

def has_digit(n, k):
    """
    Returns whether k is a digit in n.

    >>> has_digit(10,1)
    True
    >>> has_digit(12,7)
    False
    """
    assert k >= 0 and k < 10
    