# Servo Motor Control with Flask and pigpio

This project allows you to control a servo motor using a web interface built with Flask. The application takes an angle input (between 0 and 180 degrees) and moves the servo to the specified position.

## Table of Contents

- [Requirements](#requirements)
- [Hardware Setup](#hardware-setup)
- [Connection Diagram](#connection-diagram)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Usage](#usage)

## Requirements

### Hardware
- Raspberry Pi (any model with GPIO)
- Servo Motor
- Jumper Wires
- Breadboard (optional)

### Software
- Python 3
- Flask
- pigpio

## Hardware Setup

Make sure your Raspberry Pi is powered off before making connections. Connect the servo motor to the Raspberry Pi GPIO as follows:

### Connection Diagram