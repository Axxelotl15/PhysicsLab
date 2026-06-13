import numpy as np
import matplotlib.pyplot as plt

# Parameters
omega = 1.0	# angular frequency
dt = 0.01	# time step
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
	v[i+1] = v[i] - dt * omega**2 * x[i]
	x[i+1] = x[i] + dt * v[i+1]
energy = 0.5 * v**2 + 0.5 * omega**2 * x**2	
# ~ # Plot
# ~ plt.plot(t,x)
# ~ plt.xlabel("Time")
# ~ plt.ylabel("Position")
# ~ plt.title("Simple Harmonic Oscillator (Euler Method)")
# ~ plt.grid()
# ~ plt.show()

#Plot 2
plt.figure()
plt.plot(t, energy)
plt.xlabel("Time")
plt.ylabel("Energy")
plt.title("Energy vs Time")
plt.grid()
plt.show()
