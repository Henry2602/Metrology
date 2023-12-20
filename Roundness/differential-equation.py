import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the second-order ODE
def model(y, x):
    dydx = [y[1], -2*y[1] - y[0]]
    return dydx

# Set initial conditions
y0 = [1, 0]  # Initial values for y and dy/dx

# Create a time array
x = np.linspace(0, 10, 100)

# Solve the ODE
y = odeint(model, y0, x)

# Plot the solution
plt.plot(x, y[:, 0], label='y(x)')
plt.plot(x, y[:, 1], label="y'(x)")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
