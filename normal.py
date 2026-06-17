import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
xmin = -3.0
xmax = 3.0
xstep = 0.01

# Mean and variance of the normal curve
sigma = 1.0
mu = 0.0

# Calculate the normal curve
x = np.arange(xmin,xmax,xstep)
y = (1.0 / (sigma*np.sqrt(2*np.pi))) \
        * np.exp( - (x-mu)**2 / (2 * sigma**2) )

# Now we work on the graphics
#####################################################################

# Create the figure and axes for the plot   
fig, ax = plt.subplots(nrows=1, ncols=1)

# Set parameters for graph
ax.set(xlabel='x-axis', 
       ylabel='y-axis',
       title=f'Normal curve with mean {mu} and standard deviation '
             f'{sigma}')
ax.grid()

# Plot the normal curve
ax.plot(x,y)

# Show the graph
plt.show()
