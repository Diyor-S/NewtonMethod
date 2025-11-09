def solution_details(
    x0, y0,
    x_sol, y_sol,
    f1_val, f2_val,
    error
):
    print(f"\nNew solution found:")
    print(f"  Starting point: ({x0:.2f}, {y0:.2f})")
    print(f"  Solution: x = {x_sol:.6f}, y = {y_sol:.6f}")
    print(f"  Verification: f1 = {f1_val:.2e}, f2 = {f2_val:.2e}")
    print(f"  Error: {error:.2e}")
