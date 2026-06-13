import numpy as np
import matplotlib.pyplot as plt

# Parameters
omega = 1.0	# angular frequency
dt = 0.01	# time step # Changed 0.1 to 0.01
t_max = 20	# total time

# Time array
t = np.arange(0, t_max, dt)

# Arrays for position and velocity
x = np.zeros(len(t))
v = np.zeros(len(t))

# Initial conditions
x[0] = 1.0
v[0] = 0.0

# Euler Method
for i in range(len(t) - 1):
x[i+1] = x[i] + dt * v[i]
v[i+1] = v[i] - dt * omega**2 * x[i]
	
# ~ # Plot
plt.plot(t,x)
plt.xlabel("Time")
plt.ylabel("Position")
plt.title("Simple Harmonic Oscillator (Euler Method)")
plt.grid()
# ~ plt.show()

plt.grid()
plt.show()
