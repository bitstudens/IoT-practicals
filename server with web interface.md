# Servo Motor Control with Flask and pigpio

This project allows you to control a servo motor using a web interface built with Flask. The application takes an angle input (between 0 and 180 degrees) and moves the servo to the specified position.

## Table of Contents

- [Requirements](#requirements)
- [Hardware Setup](#hardware-setup)
- [Connection Diagram](#connection-diagram)
- [Installation](#installation)
- [Running the Application](#running-the-application)


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

## Connection Diagram
- Servo Motor       Raspberry Pi

- Signal Pin        GPIO 18 (Pin 12)
- Power (VCC)       5V Power (Pin 2 or 4)
- Ground (GND)      Ground (Pin 6)

## Installation

```bash
sudo apt update
sudo apt install python3-pigpio python3-flask
sudo systemctl enable pigpiod
sudo systemctl start pigpiod
```

## Running the Application

```python

from flask import Flask, render_template, request
import pigpio

app = Flask(__name__)

# Initialize pigpio and set up the GPIO pin for PWM
SERVO_PIN = 18  # GPIO pin where the signal wire is connected
pi = pigpio.pi()

# Function to move the servo to a specific angle
def set_servo_angle(angle):
    pulse_width = 500 + (angle / 180.0) * 2000  # Pulse width between 500µs and 2500µs
    pi.set_servo_pulsewidth(SERVO_PIN, pulse_width)

# Home page to control the servo
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the angle from the form and move the servo
        angle = request.form.get("angle", type=int)
        if angle is not None and 0 <= angle <= 180:
            set_servo_angle(angle)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```


### Create a folder name templates and create a file named index.html and add following code

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Servo Motor Control</title>
    <style>
        body { font-family: Arial, sans-serif; }
        .container { max-width: 500px; margin: auto; padding: 20px; }
        .control-form { display: flex; flex-direction: column; align-items: center; }
        input { margin: 10px; padding: 10px; font-size: 1.2em; }
        button { padding: 10px 20px; font-size: 1.2em; cursor: pointer; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Servo Motor Control</h1>
        <form class="control-form" method="POST">
            <label for="angle">Set Servo Angle (0-180 degrees):</label>
            <input type="number" id="angle" name="angle" min="0" max="180" required>
            <button type="submit">Move Servo</button>
        </form>
    </div>
</body>
</html>
```

### Run the program
```
python app.py
```

Good Luck
