import numpy as np
from scipy.optimize import linprog

# Documentation for linprog: https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html

# We want to minimize C =  3x0 + 4x1 + 2x2 + 5x3 + 7x5 + 8x6 + 6x7
#                        + 4x9 + 9x10 + 5x12 +3x14
          

# 1. Define the objective function coefficients
c = [3, 4, 2, 5, 0, 7, 8, 6, 0, 4, 9, 0, 5, 0, 3]

# 2 Define the equality constraints 
Aeq = [
    # x0,  x1   x2   x3   x4   x5   x6   x7   x8   x9  x10  x11  x12  x13  x14 
    [  1,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],   #x0 + x1 = 1000
    [  0,   0,   1,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],   #x2 + x3 = 1200
    [  0,   0,   0,   0,   1,   1,   1,   1,   0,   0,   0,   0,   0,   0,   0],   #x4 + x5 + x6 + x7 =2200   
    [  0,   0,   0,   0,   0,   0,   0,   0,   1,   1,   1,   0,   0,   0,   0],   #x8 + x9 + x10 = 2200
    [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   1,   0,   0],   #x11 + x12 = 2200
    [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   1],   #x13 + x14 = 2200
    [  1,   0,   1,   0,   1,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],   #x0 + x2 + x4 = 2200
    [  0,   1,   0,   1,   0,   1,   0,   0,   1,   0,   0,   0,   0,   0,   0],   #x1 + x3 + x5 + x8 = 2200
    [  0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   1,   0,   0,   0],   #x6 + x11 = 3000
    [  0,   0,   0,   0,   0,   0,   0,   1,   0,   1,   0,   0,   1,   1,   0],   #x7 + x9 + x12 + x13 = 3100
    [  0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   1]    #x10 + x14 = 500
]

beq = [1000, 1200, 2200, 2200, 2200, 2200, 2200, 2200, 3000, 3100, 500]

# 3. Define the bounds 
# x_bounds = (0, None)  # None means infinity
# y_bounds = (0, None)

# 5. Solve the linear programming problem
# We use the recommended 'highs' method for modern, fast execution
res = linprog(c, A_eq=Aeq, b_eq=beq, method='highs')

# 6. Display the results
if res.success:
    print("Optimization successful!")
    print(f"Optimal value for x0: {res.x[0]:.1f}")
    print(f"Optimal value for x1: {res.x[1]:.1f}")
    print(f"Optimal value for x2: {res.x[2]:.1f}")
    print(f"Optimal value for x3: {res.x[3]:.1f}")
    print(f"Optimal value for x4: {res.x[4]:.1f}")
    print(f"Optimal value for x5: {res.x[5]:.1f}")
    print(f"Optimal value for x6: {res.x[6]:.1f}")
    print(f"Optimal value for x7: {res.x[7]:.1f}")
    print(f"Optimal value for x8: {res.x[8]:.1f}")
    print(f"Optimal value for x9: {res.x[9]:.1f}")
    print(f"Optimal value for x10: {res.x[10]:.1f}")
    print(f"Optimal value for x11: {res.x[11]:.1f}")
    print(f"Optimal value for x12: {res.x[12]:.1f}")
    print(f"Optimal value for x13: {res.x[13]:.1f}")
    print(f"Optimal value for x14: {res.x[14]:.1f}")
    print(f"Minimum value of the objective function: {res.fun:.1f}")
else:
    print("Optimization failed:", res.message)
