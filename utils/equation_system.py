from global_v import (
    V,
    a1, a2, a3, b1, b2, b3,
)


# Define the system of equations
def f1(x, y):
    return a1 * x ** 2 + a2 * y ** 2 - a3 * x * y - V


def f2(x, y):
    return b1 * x ** 2 + b2 * y ** 2 + b3 * x * y - V
