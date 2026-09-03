# Daily Log

## May 16, 2026
    - Cloned repo and set up PlatformIO environment
## May 17, 2026
    - Installed NumPy and Matplotlib.
    - Successfully ran and saved the first plot in Python.
    - Python simulation environment is fully operational.
## May 18, 2026
    - Simulated a simple motor and controller
    - Observed how Tau, Kp, Ki, and Kd affected the simulation
    - Observed how they reacted when noise was introduced
    - Plotted simulated target vs. measured RPM
    - Found Kd wasn't needed, only a PI controller may be necessary
## May 19, 2026
    - Full Motor Circuit Built
    - Tested random PWM's
## August 12, 2026
    - Completed the code framework for the motor to run
    - Calculated RPM and Error
    - Completed PI Control
    - In order to begin collecting visual data, I used AI assistance to generate code to read serial data from the ESP32 and plot it onto a graph. I reviewed the code thoroughly to understand it how it reads the serial data from the ESP32 and plots that onto a grid.
    - Collected Graphing Data for PI Control
## August 20, 2026
    - Implemented D control, finishing full PID control
    - D term added unnecessary noise, ommitted for now
    - Took photos of circuit
## August 28, 2026
    - Tuned Kp, Ki, and Kd to a reasonable amount
    - Reached a steady state error of about 2%-4% with lower RPM's (80RPM)
    - Collected additional data
## September 2, 2026
    - Uploaded images to Github
    - Populated missing entries from daily-log.md