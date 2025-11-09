from global_v import solutions, solution_tolerance, solution_verification_threshold
from utils.equation_system import f1, f2
import numpy as np


def is_new_solution(x_sol, y_sol) -> bool:
    is_new = True
    for (xs, ys) in solutions:
        if np.sqrt((x_sol - xs) ** 2 + (y_sol - ys) ** 2) < solution_tolerance:
            is_new = False
            break
    return is_new


def _request_verify_solution(
    x_sol, y_sol
) -> tuple[float | int, float | int, float | int]:
    f1_val = f1(x_sol, y_sol)
    f2_val = f2(x_sol, y_sol)
    error = np.sqrt(f1_val ** 2 + f2_val ** 2)
    return f1_val, f2_val, error


def is_solution_verified(x_sol, y_sol):
    f1_val, f2_val, error = _request_verify_solution(x_sol, y_sol)
    return (f1_val, f2_val), error, (error < solution_verification_threshold)
