# ESP32 PID DC Motor Speed Controller

## Overview
This project uses an ESP32, a TB6612FNG motor driver, and a DC gear motor with encoder feedback to read motor speed and control it using PID control. The system measures RPM from encoder pulses, compares it to a target RPM, and adjusts the PWM output to reduce the error. The ESP32 was programmed in C++ using an Arduino framework. The project was built in Visual Studio Code using PlatformIO which was used to build and upload the code to the ESP32.

## Features
- PWM motor speed control
- Encoder-based RPM measurement
- Serial monitoring
- PID tuning
- Disturbance recovery

## Hardware Used
- ESP32 DevKit
- TB6612FNG motor driver
- TT DC gear motor with encoder (6V 160RPM 120:1)
- 6V external power supply
- Breadboard and jumper wires
- 0.1 µF capacitor across motor terminals

## Wiring
| Component | Pin / Terminal | Connects To | Purpose |
|---|---|---|---|
| ESP32 | 3V3 | Motor Driver VCC | Logic power for motor driver |
| ESP32 | 3V3 | Motor Driver STBY | Keeps motor driver enabled |
| ESP32 | GND | Motor Driver GND | Common ground |
| 6V Power Supply | + | Motor Driver VM / VMOT | Motor power |
| 6V Power Supply | - | Motor Driver GND | Motor power ground |
| ESP32 | GPIO25 / D25 | Motor Driver PWMA | PWM speed control |
| ESP32 | GPIO26 / D26 | Motor Driver AIN1 | Motor direction control |
| ESP32 | GPIO27 / D27 | Motor Driver AIN2 | Motor direction control |
| Motor Driver | AO1 | Motor + | Motor output |
| Motor Driver | AO2 | Motor - | Motor output |
| Motor Encoder | VCC | ESP32 3V3 | Encoder power |
| Motor Encoder | GND | ESP32 GND | Encoder ground |
| Motor Encoder | A | ESP32 GPIO32 / D32 | Encoder pulse input |
| 0.1 µF capacitor | One leg | Motor + | Noise suppression |
| 0.1 µF capacitor | Other leg | Motor - | Noise suppression |

## How It Works
1. ESP32 sends PWM to the motor driver
2. The driver then powers the motor
3. The encoder feedback from the motor then gets sent to the ESP32
4. The ESP32 calculates the RPM and error
5. The PID control in the ESP32 sends a new PWM to the motor driver adjusting to mitigate error

## RPM Calculation
The encoder is rated at 8 pulses per rotation. With a 120:1 gearbox ratio and using CHANGE interrupt mode
8 * 120 * 2 = 1920 pulses per shaft revolution
RPM = (pulses/1920) * (60/dt)

## Control System
The PWM is controlled through PID
The Kp term calculates the present error 
The Ki term calculates the integral error; the added up error over time
The Kd term calculates the derivative error; the rate of change of error

## Testing and Results


## Challenges
- Dealing with encoder noise
- Finding the correct PPR
- Figuring out how to properly wire the system together
- Difficulties tuning
- Difficulties setting up easily understandable output, had to convert serial output into a graph

## What I Learned
- how interrupts work
- PWM / duty cycle
- encoder feedback
- RPM calculation, PID calculation
- PID tuning
- closed-loop control

## Future Improvements
- Add improved filtering
- Create a simpler data sampling environment
- Ability to adjust target RPM as the code is still running