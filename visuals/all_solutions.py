from global_v import solutions
from utils.equation_system import f1, f2


def all_solutions_info():
    print("\n" + "=" * 60)
    print("ALL SOLUTIONS FOUND")
    print("=" * 60)

    for i, (x, y) in enumerate(solutions, 1):
        print(f"Solution {i}: x = {x:.6f}, y = {y:.6f}")
        print(f"  f1({x:.6f}, {y:.6f}) = {f1(x, y):.6e}")
        print(f"  f2({x:.6f}, {y:.6f}) = {f2(x, y):.6e}")
        print()

    print("\n" + "=" * 60)
    print(f"Total number of solutions found: {len(solutions)}")
    print("=" * 60)
