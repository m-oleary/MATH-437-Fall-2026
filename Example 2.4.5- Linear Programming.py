import numpy as np
from scipy.optimize import linprog

# Documentation for linprog: https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html

# We want to maximize P = 6.7(x11+x21) + 7.2(x12+x22) + 8.1(x13+x23)

# Define variables as follows
# x[0] = x11, x[1] = x12, x[2] = x13
# x[3] = x21, x[4] = x22, x[5] = x23


# 1. Define the objective function coefficients
# We wnt to maximize, so we minimize its negative
c = [-6.7, -7.2, -8.1, -6.7, -7.2, -8.1]

# 2 Define the inequality constraints 
Aub = [
#   x11  x12  x13  x21  x22  x23   
   [  5,   5,   5,  10,  10,  10],  # 5(x11+x12+x13) + 10(x21+x22+x23) <= 1,500,000
   [  0,   0,   0,   2,   2,   2],  # 2(x21+x22+x23) <= 200,000
   [  1,   0,   0,   1,   0,   0],  # x11 + x21 <= 50,000
   [  0,   1,   0,   0,   1,   0],  # x12 + x22 <= 30,000
   [  0,   0,   1,   0,   0,   1],  # x13 + x23 <= 40,000
   [  5,   0,   0, -11,   0,   0],  # 5x11 -11x21 <= 0
   [  0,   7,   0,   0,  -9,   0],  # 7x12 - 9x22 <= 0
   [  0,   0,  10,   0,   0,  -6]   # 10x13 - 6x23 <=0
]

bub = [1500000, 200000, 50000, 30000, 40000, 0, 0, 0]

# 3. Define the bounds 
# x_bounds = (0, None)  # None means infinity
# y_bounds = (0, None)

# 5. Solve the linear programming problem
# We use the recommended 'highs' method for modern, fast execution
res = linprog(c, A_ub=Aub, b_ub=bub, method='highs')

# 6. Display the results
if res.success:
    print("Optimization successful!")
    print(f"Optimal value for x11: {res.x[0]:.1f}")
    print(f"Optimal value for x12: {res.x[1]:.1f}")
    print(f"Optimal value for x13: {res.x[2]:.1f}")
    print(f"Optimal value for x21: {res.x[3]:.1f}")
    print(f"Optimal value for x22: {res.x[4]:.1f}")
    print(f"Optimal value for x23: {res.x[5]:.1f}")
    print(f"ON=87 production: {res.x[0]+res.x[3]:.1f}")
    print(f"ON=89 production: {res.x[1]+res.x[4]:.1f}")
    print(f"ON=92 production: {res.x[2]+res.x[5]:.1f}")
    # We negate the result back to get the maximum value
    print(f"Minimum value of the objective function: {-res.fun:.1f}")
else:
    print("Optimization failed:", res.message)