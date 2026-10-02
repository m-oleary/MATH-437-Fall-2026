import numpy as np
from scipy.optimize import linprog

# Documentation for linprog: https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html

# We want to minimize C =   40 x11 + 40.5 x12 + 41   x13 + 41.5 x14
#                         + 42 x21 + 40   x22 + 40.5 x23 + 41   x24
#                         + 44 x31 + 42   x32 + 40   x33 + 40.5 x34
#                         + 46 x41 + 44   x42 + 42   x43 + 40   x44

# 1. Define the objective function coefficients
c = [40, 40.5, 41, 41.5, 42, 40, 40.5, 41, 44, 42, 40, 40.5, 46, 44, 42, 40]

# 2 Define the equality constraints 
Aeq = [
    # x11 x12 x13 x14 x21 x22 x23 x24 x31 x32 x33 x34 x41 x42 x43 x44
    [   1,  1,  1,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],   #x11 + x12 + x13 + x14 = 50
    [   0,  0,  0,  0,  1,  1,  1,  1,  0,  0,  0,  0,  0,  0,  0,  0],   #x21 + x22 + x23 + x24 = 180
    [   0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  1,  1,  0,  0,  0,  0],   #x31 + x32 + x33 + x34 = 280
    [   0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  1,  1],   #x41 + x42 + x43 + x44 = 270
    [   1,  0,  0,  0,  1,  0,  0,  0,  1,  0,  0,  0,  1,  0,  0,  0],   #x11 + x21 + x31 + x41 = 100
    [   0,  1,  0,  0,  0,  1,  0,  0,  0,  1,  0,  0,  0,  1,  0,  0],   #x12 + x22 + x32 + x42 = 200
    [   0,  0,  1,  0,  0,  0,  1,  0,  0,  0,  1,  0,  0,  0,  1,  0],   #x13 + x23 + x33 + x43 = 180
    [   0,  0,  0,  1,  0,  0,  0,  1,  0,  0,  0,  1,  0,  0,  0,  1],   #x14 + x24 + x34 + x44 = 300
]

beq = [50, 180, 280, 270, 100, 200, 180, 300]

# 3. Define the bounds 
# x_bounds = (0, None)  # None means infinity
# y_bounds = (0, None)

# 5. Solve the linear programming problem
# We use the recommended 'highs' method for modern, fast execution
res = linprog(c, A_eq=Aeq, b_eq=beq, method='highs')

# 6. Display the results
if res.success:
    print("Optimization successful!")
    print(f"Optimal value for x11: {res.x[0]:.1f}")
    print(f"Optimal value for x12: {res.x[1]:.1f}")
    print(f"Optimal value for x13: {res.x[2]:.1f}")
    print(f"Optimal value for x14: {res.x[3]:.1f}")
    print(f"Optimal value for x21: {res.x[4]:.1f}")
    print(f"Optimal value for x22: {res.x[5]:.1f}")
    print(f"Optimal value for x23: {res.x[6]:.1f}")
    print(f"Optimal value for x24: {res.x[7]:.1f}")
    print(f"Optimal value for x31: {res.x[8]:.1f}")
    print(f"Optimal value for x32: {res.x[9]:.1f}")
    print(f"Optimal value for x33: {res.x[10]:.1f}")
    print(f"Optimal value for x34: {res.x[11]:.1f}")
    print(f"Optimal value for x41: {res.x[12]:.1f}")
    print(f"Optimal value for x42: {res.x[13]:.1f}")
    print(f"Optimal value for x43: {res.x[14]:.1f}")
    print(f"Optimal value for x44: {res.x[15]:.1f}")
    print(f"Minimum value of the objective function: {res.fun:.1f}")
else:
    print("Optimization failed:", res.message)
