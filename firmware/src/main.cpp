#include <Arduino.h>

// Motor Driver Pins
const int AIN1 = 26;
const int AIN2 = 27;
const int PWMA = 25;

// Encoder Pin
const int encoderPin = 32;

// Pulse Count
volatile long pulseCount = 0;

// PWM Settings
const int pwmChannel = 0;
const int pwmFreq = 1000;
const int pwmRes = 8;

// RPM Variables
const int sampleTimeMs = 100;
unsigned long lastSampleTime = 0;
float targetRPM = 0;

// Interrupt Function
void IRAM_ATTR countPulse() {
  pulseCount++;
}

// PID Control Variables
float errorIntegral = 0;
float previousError = 80;
bool firstDerivative = true;
float rateOfChange = 0;
float Kp = 3;
float Ki = 5;
float Kd = 0.0;
float pOutput = 0;
float iOutput = 0;
float dOutput = 0;

// Setup
void setup() {
  Serial.begin(115200);
  delay(15000);
  // Configure Motor Driver
  pinMode(AIN1, OUTPUT);
  pinMode(AIN2, OUTPUT);
  // Configure Encoder 
  pinMode(encoderPin, INPUT_PULLUP);
  attachInterrupt(encoderPin, countPulse, CHANGE);
  // Configure PWM
  ledcSetup(pwmChannel, pwmFreq, pwmRes);
  ledcAttachPin(PWMA, pwmChannel);
  // Set Motor Direction
  digitalWrite(AIN1, HIGH);
  digitalWrite(AIN2, LOW);
  // Set Motor Speed
  ledcWrite(pwmChannel, 0);
  // RPM Calculation
  lastSampleTime = millis();
}

void loop() {
  unsigned long currentTime = millis();
  if(currentTime - lastSampleTime >= sampleTimeMs){
    // Find pulse count for interval
    noInterrupts();
    long pulses = pulseCount;
    pulseCount = 0;
    interrupts();
    // Calculate RPM and Error
    float dt = (currentTime - lastSampleTime) / 1000.0;
    float rpm = 60 * (pulses / 1920.0) / dt;
    float error = targetRPM - rpm;
    if(firstDerivative) {
      firstDerivative = false;
      previousError = error;
    }
    else {
      rateOfChange = (error - previousError) / dt;
      previousError = error;
    }
    errorIntegral += error * dt;
    lastSampleTime = currentTime;
    // PID Control
    pOutput = Kp * error;
    iOutput = constrain(Ki * errorIntegral, -255, 255);
    dOutput = Kd * rateOfChange;
    int pwmOutput = constrain(pOutput + iOutput + dOutput, 0, 255);
    ledcWrite(pwmChannel, pwmOutput);
    Serial.printf("%.2f,%.2f\n", targetRPM, rpm);
  }
}
