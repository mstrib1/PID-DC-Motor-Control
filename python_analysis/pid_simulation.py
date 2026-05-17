import numpy as np
import matplotlib.pyplot as plt

# Sample time data (seconds)
t = np.array([
    0, 0.5, 1.0, 1.5, 2.0,
    2.5, 3.0, 3.5, 4.0, 4.5,
    5.0, 5.5, 6.0, 6.5, 7.0,
    7.5, 8.0, 8.5, 9.0, 9.5, 10.0
])

# Simulated measured motor speed (RPM)
rpm = np.array([
     0, 12, 28, 45, 60,
    72, 81, 88, 93, 96,
    98, 99, 100, 100, 100,
   100, 100, 100, 100, 100, 100
])

# Target speed (constant 100 RPM)
target_rpm = np.ones_like(t) * 100

# Plot both curves
plt.plot(t, rpm, label="Measured RPM")
plt.plot(t, target_rpm, "--", label="Target RPM")

# Labels and formatting
plt.xlabel("Time (s)")
plt.ylabel("RPM")
plt.title("Simulated Motor Step Response")
plt.legend()
plt.grid(True)

# Show the plot
plt.show()