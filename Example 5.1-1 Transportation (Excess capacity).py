import numpy as np
from scipy.optimize import linprog

# Documentation for linprog: https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html

# We want to minimize C = 80 x11 + 215 x12 + 100 x21 + 108 x22 + 102 x31 + 68 x32

# 1. Define the objective function coefficients
c = [80, 215, 100, 108, 102, 68]

# 2 Define the upper bounds

Aub = [
    [1, 1, 0, 0, 0, 0],     # x11 + x12 <= 1000
    [0, 0, 1, 1, 0, 0],     # x21 + x22 <= 2000
    [0, 0, 0, 0, 1, 1],     # x31 + x32 <= 1200
]

bub = [1000, 2000, 1200]

#
# Define the equality constraints 

Aeq = [
   [  1, 0, 1, 0, 1, 0],  # x11 + x21 + x31 = 2300
   [  0, 1, 0, 1, 0, 1],  # x12 + x22 + x32 = 1400
]

beq = [2300, 1400]

# 3. Define the bounds 
# x_bounds = (0, None)  # None means infinity
# y_bounds = (0, None)

# 5. Solve the linear programming problem
# We use the recommended 'highs' method for modern, fast execution
res = linprog(c, A_ub=Aub, b_ub=bub, A_eq=Aeq, b_eq=beq, method='highs')

# 6. Display the results
if res.success:
    print("Optimization successful!")
    print(f"Optimal value for x11: {res.x[0]:.1f}")
    print(f"Optimal value for x12: {res.x[1]:.1f}")
    print(f"Optimal value for x21: {res.x[2]:.1f}")
    print(f"Optimal value for x22: {res.x[3]:.1f}")
    print(f"Optimal value for x31: {res.x[4]:.1f}")
    print(f"Optimal value for x32: {res.x[5]:.1f}")
    print(f"Minimum value of the objective function: {res.fun:.1f}")
else:
    print("Optimization failed:", res.message)
