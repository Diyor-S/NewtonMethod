from utils.jacobian_det_and_deltas import (
    Delta,
    Delta_x,
    Delta_y
)
import numpy as np


# Newton's method
def newton_method(x0, y0, epsilon, max_iter=100):
    x, y = x0, y0
    iterations = []

    for k in range(max_iter):
        iterations.append((x, y))

        delta = Delta(x, y)
        if abs(delta) < 1e-10:
            print(f"Warning: Jacobian determinant too small at iteration {k}")
            return None, iterations

        dx = Delta_x(x, y) / delta
        dy = Delta_y(x, y) / delta

        x_new = x - dx
        y_new = y - dy

        # Check stopping condition
        distance = np.sqrt((x_new - x) ** 2 + (y_new - y) ** 2)

        x, y = x_new, y_new

        if distance < epsilon:
            iterations.append((x, y))
            print(f"  Converged in {k + 1} iterations")
            return (x, y), iterations

    print(f"  Did not converge in {max_iter} iterations")
    return None, iterations
