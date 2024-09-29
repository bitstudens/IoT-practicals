# LED Brightness Control with Flask and pigpio

This project allows you to control the brightness of an LED using a web interface built with Flask. The application lets you select different brightness levels (0%, 25%, 50%, 75%, and 100%) for an LED connected to a Raspberry Pi.

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
- LED
- Resistor (appropriate value for your LED, e.g., 220 ohms)
- Breadboard (optional)
- Jumper Wires

### Software
- Python 3
- Flask
- pigpio

## Hardware Setup

Make sure your Raspberry Pi is powered off before making connections. Connect the LED to the Raspberry Pi GPIO as follows:

### Connection Diagram
LED Pin          Raspberry Pi Pin
- Anode (longer)   GPIO 18 (Pin 12) - Through a resistor (e.g., 220 ohms)
- Cathode (shorter) Ground (GND, Pin 6)

```
pip install flask pigpio
```
### Code

```
from flask import Flask, render_template, request
import pigpio

app = Flask(__name__)

# Initialize pigpio and set up the GPIO pin for PWM
LED_PIN = 18  # GPIO pin where the LED is connected
pi = pigpio.pi()

# Function to set LED brightness
def set_led_brightness(level):
    duty_cycle = int((level / 100.0) * 255)  # Map level (0-100) to duty cycle (0-255)
    pi.set_PWM_dutycycle(LED_PIN, duty_cycle)

# Home page to control the LED
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the brightness level from the form and set the LED brightness
        brightness = request.form.get("brightness", type=int)
        if brightness is not None and 0 <= brightness <= 100:
            set_led_brightness(brightness)
    return render_template("led.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

### create a folder named templates and create a file named led.html

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LED Control</title>
    <style>
        body { font-family: Arial, sans-serif; }
        .container { max-width: 500px; margin: auto; padding: 20px; }
        .control-form { display: flex; flex-direction: column; align-items: center; }
        .radio-group { margin: 10px 0; }
        button { padding: 10px 20px; font-size: 1.2em; cursor: pointer; }
    </style>
</head>
<body>
    <div class="container">
        <h1>LED Control</h1>
        <form class="control-form" method="POST">
            <label for="brightness">Select LED Brightness:</label>
            <div class="radio-group">
                <label><input type="radio" name="brightness" value="0" required> Off</label>
                <label><input type="radio" name="brightness" value="25"> Dim</label>
                <label><input type="radio" name="brightness" value="50"> Medium</label>
                <label><input type="radio" name="brightness" value="75"> Bright</label>
                <label><input type="radio" name="brightness" value="100"> Full Brightness</label>
            </div>
            <button type="submit">Set Brightness</button>
        </form>
    </div>
</body>
</html>

```

## Usage

	1.	Select LED Brightness
On the web interface, choose a brightness level (0%, 25%, 50%, 75%, or 100%) and press the “Set Brightness” button.
	2.	Observe the LED
The LED will light up with the specified brightness level based on your input.

### Access the Web Interface
Open your web browser and navigate to http://<Raspberry-Pi-IP>:5000/. For local access, use http://localhost:5000/.

