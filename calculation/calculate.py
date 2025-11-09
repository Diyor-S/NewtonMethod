from global_v import (
    epsilon,
    x_starts, y_starts,
    solutions
)

from .newton_method import newton_method
from .__helpers import (
    is_new_solution,
    is_solution_verified,
)
from visuals.solution_detail_visuals import solution_details


def calculation_handler():
    for x0 in x_starts:
        for y0 in y_starts:
            result, iters = newton_method(x0, y0, epsilon, max_iter=50)

            if result is not None:
                x_sol, y_sol = result

                # Check if this is a new solution
                is_new_sol = is_new_solution(x_sol, y_sol)

                if is_new_sol:
                    # Verify the solution
                    (f1_val, f2_val), error, verified = is_solution_verified(x_sol, y_sol)
                    if verified:
                        solutions.append((x_sol, y_sol))
                        solution_details(
                            x0, y0,
                            x_sol, y_sol,
                            f1_val, f2_val,
                            error
                        )
