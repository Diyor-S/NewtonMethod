from .equation_system import f1, f2
from .partial_derivatives import (
    df1_dx, df1_dy,
    df2_dx, df2_dy
)


# Jacobian determinant and deltas
def Delta(x, y):
    return df1_dx(x, y) * df2_dy(x, y) - df1_dy(x, y) * df2_dx(x, y)


def Delta_x(x, y):
    return f1(x, y) * df2_dy(x, y) - f2(x, y) * df1_dy(x, y)


def Delta_y(x, y):
    return df1_dx(x, y) * f2(x, y) - df2_dx(x, y) * f1(x, y)
