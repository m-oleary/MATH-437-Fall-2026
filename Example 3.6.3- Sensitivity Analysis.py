import numpy as np
from scipy.optimize import linprog

# Documentation for linprog: https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html

# We want to maximize P = 3x1 + 2x2 + 5x3

# 1. Define the objective function coefficients
# We wnt to maximize, so we minimize its negative
c = [-3, -2, -5]

# 2 Define the inequality constraints 
Aub = [
   [  1, 2, 1],  #  x1 + 2x2 +  x3 <= 430
   [  3, 0, 2],  # 3x1       + 2x3 <= 460
   [  1, 4, 0],  #  x1 + 4x2       <= 420
]

bub = [430, 460, 420]

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
    print(f"Optimal value for x3: {res.x[2]:.1f}")
    # We negate the result back to get the maximum value
    print(f"Maximum value of the objective function: {-res.fun:.1f}")
    # See https://docs.scipy.org/doc/scipy/reference/optimize.linprog-highs.html for documentation!
    print("\nShadow prices (marginals) for constraints:")
    print("Constraint 1 (x1 + 2x2 +  x3 <= 430):", -res.ineqlin.marginals[0])
    print("Constraint 2 (x1       + 2x3 <= 460):", -res.ineqlin.marginals[1])
    print("Constraint 3 (x1 + 4x2       <= 420):", -res.ineqlin.marginals[2])
else:
    print("Optimization failed:", res.message)