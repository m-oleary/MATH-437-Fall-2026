import numpy as np
from scipy.optimize import linprog

# 1. Define the objective function coefficients
# We want to maximize .0.045935 x1 + 0.045175 x2 + 0.0486 x3 + 0.052706 x4 + 0.033125 x5
# which is equivalent to minimizing its negative
c = [-0.045935, -0.045175, -0.0486, -0.052706, -0.033125]

# 2. Define the inequality constraints (A_ub * [x, y] <= b_ub)
A = [
    [1, 1, 1, 1, 1],
    [.333,-.667,-.667,-.667,.333],
    [-.40,-.40, .60, .60, -.40],
    [.25, -.75, -.75, -.75, .25],
    [-.03, -.01, -.02, .02, .01]
]

b = [12, 0, 0, 0, 0]

# 3. Define the bounds for x and y (x >= 0, y >= 0)
# x_bounds = (0, None)  # None means infinity
# y_bounds = (0, None)

# 4. Solve the linear programming problem
# We use the recommended 'highs' method for modern, fast execution
res = linprog(c, A_ub=A, b_ub=b, method='highs')

# 5. Display the results
if res.success:
    print("Optimization successful!")
    print(f"Optimal value for x1: {res.x[0]:.4f}")
    print(f"Optimal value for x2: {res.x[1]:.4f}")
    print(f"Optimal value for x3: {res.x[2]:.4f}")
    print(f"Optimal value for x4: {res.x[3]:.4f}")
    print(f"Optimal value for x5: {res.x[4]:.4f}")
    # We negate the result back to get the maximum value
    print(f"Maximum value of the objective function: {-res.fun:.4f}")
else:
    print("Optimization failed:", res.message)