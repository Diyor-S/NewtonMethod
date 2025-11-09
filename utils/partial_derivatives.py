from global_v import (
    a1, a2, a3, b1, b2, b3
)


# Partial derivatives
def df1_dx(x, y):
    return 2 * a1 * x - a3 * y


def df1_dy(x, y):
    return 2 * a2 * y - a3 * x


def df2_dx(x, y):
    return 2 * b1 * x + b3 * y


def df2_dy(x, y):
    return 2 * b2 * y + b3 * x
