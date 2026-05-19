import numpy as np
import matplotlib.pyplot as plt


# ----------------------------
# Simulation settings
# ----------------------------
dt = 0.01              # time step in seconds
total_time = 15        # total simulation time in seconds
time = np.arange(0, total_time, dt)


# ----------------------------
# Motor model settings
# ----------------------------
motor_gain = 1.2       # RPM per PWM unit
tau = 0.5              # motor time constant in seconds

max_pwm = 255
min_pwm = 0


# ----------------------------
# PID gains
# ----------------------------
Kp = 0.1
Ki = 0.4
Kd = 0


# ----------------------------
# Target RPM
# ----------------------------
target_rpm = np.zeros_like(time)

for i, t in enumerate(time):
    if t >= 0:
        target_rpm[i] = 200   # step from 0 RPM to 200 RPM at t = 0s


# ----------------------------
# Storage arrays
# ----------------------------
measured_rpm = np.zeros_like(time)
pwm_output = np.zeros_like(time)
error_array = np.zeros_like(time)


# ----------------------------
# PID variables
# ----------------------------
integral = 0
previous_error = 0


# ----------------------------
# Simulation loop
# ----------------------------
for i in range(1, len(time)):
    # Add fake sensor/encoder noise to the RPM measurement
    noise = np.random.normal(0, 10)  # mean = 0, standard deviation = 3 RPM
    rpm_for_controller = measured_rpm[i - 1] + noise

    # Current error using noisy measured RPM
    error = target_rpm[i] - rpm_for_controller

    # PID terms
    integral += error * dt
    derivative = (error - previous_error) / dt

    # PID output
    pwm = Kp * error + Ki * integral + Kd * derivative

    # Limit PWM to valid range
    pwm = np.clip(pwm, min_pwm, max_pwm)

    # Simple motor model:
    # dRPM/dt = (motor_gain * pwm - current_rpm) / tau
    rpm_derivative = (motor_gain * pwm - measured_rpm[i - 1]) / tau

    # Update measured RPM
    measured_rpm[i] = measured_rpm[i - 1] + rpm_derivative * dt

    # Save values
    pwm_output[i] = pwm
    error_array[i] = error

    # Update previous error
    previous_error = error


# ----------------------------
# Plot target vs measured RPM
# ----------------------------
plt.figure()
plt.plot(time, target_rpm, label="Target RPM")
plt.plot(time, measured_rpm, label="Measured RPM")
plt.xlabel("Time (seconds)")
plt.ylabel("RPM")
plt.title("PID-Controlled DC Motor Speed Simulation")
plt.legend()
plt.grid(True)
plt.show()


# ----------------------------
# Plot PWM output
# ----------------------------
plt.figure()
plt.plot(time, pwm_output, label="PWM Output")
plt.xlabel("Time (seconds)")
plt.ylabel("PWM")
plt.title("Controller Output")
plt.legend()
plt.grid(True)
plt.show()


# ----------------------------
# Plot error
# ----------------------------
plt.figure()
plt.plot(time, error_array, label="Error")
plt.xlabel("Time (seconds)")
plt.ylabel("RPM Error")
plt.title("Speed Error Over Time")
plt.legend()
plt.grid(True)
plt.show()