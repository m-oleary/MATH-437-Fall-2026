import numpy as np
import matplotlib.pyplot as plt
from math import erf, sqrt

# ------------------------------------------------------------
# Define the normal probability density function
def normal(x, mu, sigma):
    return (1.0 / (sigma * np.sqrt(2 * np.pi))) * np.exp(
        - (x - mu)**2 / (2 * sigma**2)
    )

# ------------------------------------------------------------
# Set seed for reproducibility
np.random.seed(0)

# Parameters of the normal distribution
mu = 0.5
sigma = 0.8

# ------------------------------------------------------------
# Create x-values for plotting the curve
xmin = -3.0
xmax = 3.0
xstep = 0.01
x = np.arange(xmin, xmax, xstep)
y = normal(x, mu, sigma)

# ------------------------------------------------------------
# Monte Carlo sampling

n_samples = 400

# Define the sampling region
xleft= -1.0
xright = 2.0
ybottom = 0.0
ytop = 1.05 * np.max(y)

# Generate random sample points (vectorized)
x_samples = np.random.uniform(xleft, xright, n_samples)
y_samples = np.random.uniform(ybottom, ytop, n_samples)

# Determine which points are below the curve
# (NumPy evaluates this element-by-element)
below_curve = y_samples < normal(x_samples, mu, sigma)

# Fraction of points below the curve
frac_below = np.mean(below_curve)

# Monte Carlo estimate of the area
estimate = (xright - xleft) * (ytop - ybottom) * frac_below

# ------------------------------------------------------------
# Exact value using the error function
exact_value = 0.5 * (
    erf((xright - mu) / (sqrt(2) * sigma)) -
    erf((xleft - mu) / (sqrt(2) * sigma))
)

# ------------------------------------------------------------
# Plotting

fig, ax = plt.subplots()

ax.grid()
ax.set_xlim(xmin, xmax)
ax.set_ylim(0, ytop)

ax.set_title(
    f"$\\mu={mu:.3f}, \\sigma={sigma:.3f}$, N={n_samples}\n"
    f"Exact value = {exact_value:.4f}  Estimate = {estimate:.4f}"
)

# Plot the normal curve
ax.plot(x, y, label="Normal PDF")

# Color points: 0 = below, 1 = above
colors = np.where(below_curve, 0, 1)

# Scatter plot of samples
ax.scatter(x_samples, y_samples, c=colors, cmap="Set1", s=15)

ax.legend()

plt.show()
