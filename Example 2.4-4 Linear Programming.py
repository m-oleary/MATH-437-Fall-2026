import numpy as np
from scipy.optimize import linprog

# Documentation for linprog: https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html

# We want to minimize C = 50 I1 + 50 I2 + 50 I_3 + 200 H1 + 200 H2 + 200 H3 + 200 H4 + 400 F1 + 400 F2 + 400 F3 + 400 F4

# Define variables as follows
# x[0] = x1, x[1] = x2, x[2] = x3, x[3] = x4,
# x[4] = I1, x[5] = I2, x[6] = I3
# x[7] = H1, x[8] = H2, x[9] = H3, x[10] = H4
# x[11] = F1, x[12] = F2, x[13] = F3, x[14] = F4


# 1. Define the objective function coefficients
c = [0, 0, 0, 0, 50, 50, 50, 200, 200, 200, 200, 400, 400, 400, 400]

# 2 Define the equality constraints 
# Aeq = [
# #     x1  x2  x3  x4  I1  I2  I3  H1  H2  H3  H4  F1  F2  F3   F4
#     [ 10,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
#     [  0, 10,  0,  0,  1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0],
#     [  0,  0, 10,  0,  0,  1, -1,  0,  0,  0,  0,  0,  0,  0,  0],
#     [  0,  0,  0, 10,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0],
#     [  1,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0, -1,  0,  0,  0],
#     [ -1,  1,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0, -1,  0,  0],
#     [  0, -1,  1,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0, -1,  0],
#     [  0,  0, -1,  1,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0, -1]
# ]

Aeq = [
#     x1   x2   x3   x4   I1   I2   I3   H1   H2   H3   H4   F1   F2   F3   F4
    [ 10,   0,   0,   0,  -1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # 10 x1 - I1 = 400
    [  0,  10,   0,   0,   1,  -1,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # 10 x2 + I1 - I2 = 600
    [  0,   0,  10,   0,   0,   1,  -1,   0,   0,   0,   0,   0,   0,   0,   0],  # 10 x3 + I2 - I3 = 400
    [  0,   0,   0,  10,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0],  # 10 x4 + I3 = 500
    [  1,   0,   0,   0,   0,   0,   0,  -1,   0,   0,   0,   1,   0,   0,   0],  # x1 = H1 - F1
    [ -1,   1,   0,   0,   0,   0,   0,   0,  -1,   0,   0,   0,   1,   0,   0],  # x2 = x1 + H2 - F2
    [  0,  -1,   1,   0,   0,   0,   0,   0,   0,  -1,   0,   0,   0,   1,   0],  # x3 = x2 + H3 - F3
    [  0,   0,  -1,   1,   0,   0,   0,   0,   0,   0,  -1,   0,   0,   0,   1]   # x4 = x3 + H4 - F4
]

beq = [400, 600, 400, 500, 0, 0, 0, 0]

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
    print(f"Optimal value for I1: {res.x[4]:.1f}")
    print(f"Optimal value for I2: {res.x[5]:.1f}")
    print(f"Optimal value for I3: {res.x[6]:.1f}")
    print(f"Optimal value for H1: {res.x[7]:.1f}")
    print(f"Optimal value for H2: {res.x[8]:.1f}")
    print(f"Optimal value for H3: {res.x[9]:.1f}")
    print(f"Optimal value for H4: {res.x[10]:.1f}")
    print(f"Optimal value for F1: {res.x[11]:.1f}")
    print(f"Optimal value for F2: {res.x[12]:.1f}")
    print(f"Optimal value for F3: {res.x[13]:.1f}")
    print(f"Optimal value for F4: {res.x[14]:.1f}")
    # We negate the result back to get the maximum value
    print(f"Minimum value of the objective function: {res.fun:.1f}")
else:
    print("Optimization failed:", res.message)

