def sum_odd_squares_iterative(n: int) -> int:
    """
    Returns the sum of all the digits of non-negative integer n,
    except for digits in odd positions
    (starting with position 0 as the rightmost digit and moving left),
    square the digit. Implement this iteratively.

    >>> sum_odd_squares_iterative(5)
    5
    >>> sum_odd_squares_iterative(123) # 1 + (2*2) + 3 = 1 + 4 + 3 = 8
    8
    >>> sum_odd_squares_iterative(243580) # (2*2) + 4 + (3*3) + 5 + (8*8) + 0 = 4 + 4 + 9 + 5 + 64 + 0 = 86
    86
    """
    position = 0
    total = 0
    while n != 0:
        digit = n % 10
        if position % 2 == 0:
            total += digit
        else:
            total += (digit ** 2)
        n = n // 10
        position += 1
    return total


def sum_odd_squares_recursive(n: int) -> int:
    """
    Returns the sum of all the digits of non-negative integer n,
    except for digits in odd positions
    (starting with position 0 as the rightmost digit and moving left),
    square the digit. Implement this recursively.

    >>> sum_odd_squares_recursive(5)
    5
    >>> sum_odd_squares_recursive(123) # 1 + (2*2) + 3 = 1 + 4 + 3 = 8
    8
    >>> sum_odd_squares_recursive(243580) # (2*2) + 4 + (3*3) + 5 + (8*8) + 0 = 4 + 4 + 9 + 5 + 64 + 0 = 86
    86
    """
    def helper(n: int, is_odd: bool) -> int:
        if n == 0:
            return 0
        elif is_odd:
            return (n % 10) ** 2 + helper(n // 10, False)
        else:
            return n % 10 + helper(n // 10, True)
    return helper(n, False)


def count_stairs(n: int) -> int:
    """You are walking up n stairs and you may either take 1 step or 2 steps as you go.
    How many different ways can you reach the top?

    >>> count_stairs(3) # take 2 then 1; 1 then 2; OR 1, 1, 1
    3
    >>> count_stairs(2) # take 2 steps OR take 1 step twice
    2
    >>> count_stairs(4)
    5
    """
    # YOUR CODE HERE
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return count_stairs(n - 2) + count_stairs(n - 1)

def mario_number(level: int) -> int:
    """
    >>> mario_number(10101) # jump, jump
    1
    >>> mario_number(11101) # Left to right: step, step, jump OR jump, jump
    2
    >>> mario_number(100101)
    0
    """
    # YOUR CODE HERE
    if level == 1:
        return 1
    elif level % 10 == 0:
        return 0
    else:
        step = mario_number(level // 10)
        jump = mario_number(level // 100)
        return step + jump