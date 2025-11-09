import numpy as np

# Variant number
V = 18

# Accuracy
epsilon = V * 0.0001

# Coefficients for the system
a1 = (V + 1) / 2  # 9.5
a2 = (V + 2) / 4  # 5.0
a3 = (V + 3) / 5  # 4.2
b1 = (V + 2) / 5  # 4.0
b2 = (V + 3) / 3  # 7.0
b3 = (V + 5) / 4  # 5.75


# Generate grid of starting points
grid_range = 5
grid_points = 15
x_starts = np.linspace(-grid_range, grid_range, grid_points)
y_starts = np.linspace(-grid_range, grid_range, grid_points)

solutions = []
solution_tolerance = 0.1  # To identify unique solutions
solution_verification_threshold = 0.01
