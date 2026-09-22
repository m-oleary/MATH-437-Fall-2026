import numpy as np
from scipy.optimize import linprog

# Documentation for linprog: https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html

# We want to maximize P = 30 x1 + 20 x2

# 1. Define the objective function coefficients
# We wnt to maximize, so we minimize its negative
c = [-30, -20]

# 2 Define the inequality constraints 
Aub = [
   [  2, 1],  # 2x1 +  x2 <= 8
   [  1, 3], #   x1 + 3x2 <= 8
]

bub = [8,8]

# 3. Define the bounds 
# x_bounds = (0, None)  # None means infinity
# y_bounds = (0, None)

# 5. Solve the linear programming problem
# We use the recommended 'highs' method for modern, fast execution
res = linprog(c, A_ub=Aub, b_ub=bub, method='highs')

# 6. Display the results
if res.success:
    print("Optimization successful!")
    print(f"Optimal value for x1: {res.x[0]:.1f}")
    print(f"Optimal value for x2: {res.x[1]:.1f}")
    # We negate the result back to get the maximum value
    print(f"Maximum value of the objective function: {-res.fun:.1f}")
    print("\nShadow prices (marginals) for constraints:")
    print("Constraint 1 (2x1 + x2 <= 8):", -res.ineqlin.marginals[0])
    print("Constraint 2 (x1 + 3x2 <= 8):", -res.ineqlin.marginals[1])
else:
    print("Optimization failed:", res.message)