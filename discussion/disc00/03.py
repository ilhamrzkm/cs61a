"""
Imagine you can call only the following three functions:
f(x): Subtracts one from an integer x
g(x): Double an integer x
h(x, y): Concatenates digits of two different positive integers x and y.
"""


def f(x):
    return x - 1

def g(x):
    return x * 2

def h(x, y):
    return str(x) + str(y)


x = 5

print(h(g(g(x)), h(f(f(f(x))), f(x))))