import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from collections import deque
import time

# Serial settings
PORT = "COM3"
BAUD = 115200

ser = serial.Serial(PORT, BAUD, timeout=1)

# Give ESP32 a moment after opening the serial connection
time.sleep(2)

# Number of measurements visible at once
max_points = 200

times = deque(maxlen=max_points)
targets = deque(maxlen=max_points)
rpms = deque(maxlen=max_points)

start_time = time.time()

# Create graph
fig, ax = plt.subplots()

target_line, = ax.plot([], [], label="Target RPM")
rpm_line, = ax.plot([], [], label="Measured RPM")

ax.set_xlabel("Time (s)")
ax.set_ylabel("RPM")
ax.set_title("Live DC Motor Speed")
ax.legend()
ax.grid(True)


def update(frame):

    while ser.in_waiting:

        line = ser.readline().decode("utf-8").strip()

        try:
            target, rpm = map(float, line.split(","))

            elapsed = time.time() - start_time

            times.append(elapsed)
            targets.append(target)
            rpms.append(rpm)

        except ValueError:
            pass

    if len(times) > 0:

        target_line.set_data(times, targets)
        rpm_line.set_data(times, rpms)

        ax.relim()
        ax.autoscale_view()

    return target_line, rpm_line


anim = FuncAnimation(
    fig,
    update,
    interval=100,
    cache_frame_data=False
)

plt.show()

ser.close()