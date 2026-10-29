import numpy as np
from scipy.optimize import linprog

# Variables
# x0   x1   x2   x3   x4   x5   x6   x7   x8
# x12  x13  x14  x23  x25  x34  x35  x43  x45  

# 1. Define the objective function coefficients
# We want to maximize z1 = x12 + x13 + x14
# which is equivalent to minimizing its negative
c = [-1, -1, -1,  0,  0,  0,  0,  0,  0]

# We could instead try maximizing z2 = x25 + x35 + x45
# c = [0,  0,  0,  0, -1,  0, -1,  0, -1]

# 2. Define the inequality constraints (A_ub * [x, y] <= b_ub)
A = [
    # x12  x13  x14  x23  x25  x34  x35  x43  x45
    [   1,   0,   0,   0,   0,   0,   0,   0,   0],
    [   0,   1,   0,   0,   0,   0,   0,   0,   0],
    [   0,   0,   1,   0,   0,   0,   0,   0,   0],
    [   0,   0,   0,   1,   0,   0,   0,   0,   0],
    [   0,   0,   0,   0,   1,   0,   0,   0,   0],
    [   0,   0,   0,   0,   0,   1,   0,   0,   0],
    [   0,   0,   0,   0,   0,   0,   1,   0,   0],
    [   0,   0,   0,   0,   0,   0,   0,   1,   0],
    [   0,   0,   0,   0,   0,   0,   0,   0,   1],
    ]
    # x12  x13  x14  x23  x25  x34  x35  x43  x45
b = [  20,  30,  10,  40,  30,  10,  20,   5,  20]

# 3 Define the equality constraints 
Aeq = [
    # x12  x13  x14  x23  x25  x34  x35  x43  x45
    [   1,   0,   0,  -1,  -1,   0,   0,   0,   0],
    [   0,   1,   0,   1,   0,  -1,  -1,   1,   0],
    [   0,   0,   1,   0,   0,   1,   0,  -1,  -1]
]

beq = [0, 0, 0]

# 4. Define the bounds 
# x_bounds = (0, None)  # None means infinity
# y_bounds = (0, None)

# 5. Solve the linear programming problem
# We use the recommended 'highs' method for modern, fast execution
res = linprog(c, A_ub=A, b_ub=b, A_eq=Aeq, b_eq=beq, method='highs')

# 6. Display the results
if res.success:
    print("Optimization successful!")
    print(f"Optimal value for x12: {res.x[0]:.1f}")
    print(f"Optimal value for x13: {res.x[1]:.1f}")
    print(f"Optimal value for x14: {res.x[2]:.1f}")
    print(f"Optimal value for x23: {res.x[3]:.1f}")
    print(f"Optimal value for x25: {res.x[4]:.1f}")
    print(f"Optimal value for x34: {res.x[5]:.1f}")
    print(f"Optimal value for x35: {res.x[6]:.1f}")
    print(f"Optimal value for x43: {res.x[7]:.1f}")
    print(f"Optimal value for x45: {res.x[7]:.1f}")
    # We negate the result back to get the maximum value
    print(f"Maximum flow rate: {-res.fun:.1f}")
else:
    print("Optimization failed:", res.message)