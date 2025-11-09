from global_v import (
    V, epsilon,
    a1, a2, a3, b1, b2, b3,
)


def task_info():
    print(f"Variant: {V}")
    print(f"Accuracy ε = {epsilon}\n")

    print("System of equations:")
    print(f"{a1}x² + {a2}y² - {a3}xy = {V}")
    print(f"{b1}x² + {b2}y² + {b3}xy = {V}\n")
