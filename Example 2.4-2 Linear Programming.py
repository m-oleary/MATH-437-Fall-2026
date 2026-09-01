import numpy as np
from scipy.optimize import linprog

# 1. Define the objective function coefficients
# We want to maximize P = 30 x1 + 40 x2 + 20 x3 + 10 x4 - 15 s1 - 20 s2 -10 s3 - 8 s4
# which is equivalent to minimizing its negative
c = [-30, -40, -20, -10, 15, 20, 10, 8]

# 2. Define the inequality constraints (A_ub * [x, y] <= b_ub)
A = [
    [0.30, 0.30, 0.25, 0.15, 0, 0, 0, 0],
    [0.25, 0.35, 0.30, 0.10, 0, 0, 0, 0],
    [0.45, 0.50, 0.40, 0.22, 0, 0, 0, 0],
    [0.15, 0.15, 0.10, 0.05, 0, 0, 0, 0]
    ]
b = [1000, 1000, 1000, 1000]

# 3 Define the equality constraints 
Aeq = [
    [1, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 1]
]

beq = [800, 750, 600, 500]

# 4. Define the bounds 
# x_bounds = (0, None)  # None means infinity
# y_bounds = (0, None)

# 5. Solve the linear programming problem
# We use the recommended 'highs' method for modern, fast execution
res = linprog(c, A_ub=A, b_ub=b, A_eq=Aeq, b_eq=beq, method='highs')

# 6. Display the results
if res.success:
    print("Optimization successful!")
    print(f"Optimal value for x1: {res.x[0]:.1f}")
    print(f"Optimal value for x2: {res.x[1]:.1f}")
    print(f"Optimal value for x3: {res.x[2]:.1f}")
    print(f"Optimal value for x4: {res.x[3]:.1f}")
    print(f"Optimal value for s1: {res.x[4]:.1f}")
    print(f"Optimal value for s2: {res.x[5]:.1f}")
    print(f"Optimal value for s3: {res.x[6]:.1f}")
    print(f"Optimal value for s4: {res.x[7]:.1f}")
    # We negate the result back to get the maximum value
    print(f"Maximum value of the objective function: {-res.fun:.1f}")
else:
    print("Optimization failed:", res.message)