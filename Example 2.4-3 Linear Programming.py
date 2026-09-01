import numpy as np
from scipy.optimize import linprog

# 1. Define the objective function coefficients
# We want to minimize C = 50 x1 + 45 x2 + 55 x3 + 48 x4 + 52 x5 + 50 x6 + 8 I1 + 8 I2 + 8 I3 + 8 I4 + 8 I5 + 8 I6
c = [50, 45, 55, 48, 52, 50, 8, 8, 8, 8, 8, 8]

# 2 Define the equality constraints 
Aeq = [
    [1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, -1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, -1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, -1, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0]
]

beq = [100, 250, 190, 140, 220, 110]

# 3. Define the bounds 
# x_bounds = (0, None)  # None means infinity
# y_bounds = (0, None)

# 5. Solve the linear programming problem
# We use the recommended 'highs' method for modern, fast execution
res = linprog(c, A_eq=Aeq, b_eq=beq, method='highs')

# 6. Display the results
if res.success:
    print("Optimization successful!")
    print(f"Optimal value for x1: {res.x[0]:.1f}")
    print(f"Optimal value for x2: {res.x[1]:.1f}")
    print(f"Optimal value for x3: {res.x[2]:.1f}")
    print(f"Optimal value for x4: {res.x[3]:.1f}")
    print(f"Optimal value for x5: {res.x[4]:.1f}")
    print(f"Optimal value for x6: {res.x[5]:.1f}")
    print(f"Optimal value for I1: {res.x[6]:.1f}")
    print(f"Optimal value for I2: {res.x[7]:.1f}")
    print(f"Optimal value for I3: {res.x[8]:.1f}")
    print(f"Optimal value for I4: {res.x[9]:.1f}")
    print(f"Optimal value for I5: {res.x[10]:.1f}")
    print(f"Optimal value for I6: {res.x[11]:.1f}")
    # We negate the result back to get the maximum value
    print(f"Minimum value of the objective function: {res.fun:.1f}")
else:
    print("Optimization failed:", res.message)
