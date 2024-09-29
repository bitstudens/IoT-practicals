# LED Brightness Control with Flask, pigpio, and AJAX

This project allows you to control the brightness of an LED connected to a Raspberry Pi using a web interface built with Flask. The application features a slider to dynamically adjust brightness levels (0-100%) using AJAX requests.

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

| LED Pin        | Raspberry Pi Pin           |
| -------------- | -------------------------- |
| Anode (longer) | GPIO 18 (Pin 12) - Through a resistor (e.g., 220 ohms) |
| Cathode (shorter) | Ground (GND, Pin 6) |

The resistor is necessary to limit the current flowing through the LED and prevent damage.

## Installation

```
pip install flask pigpio
```

### Code

```
from flask import Flask, render_template, request, jsonify
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
@app.route("/", methods=["GET"])
def index():
    return render_template("led_slider.html")

# AJAX endpoint to set brightness
@app.route("/set_brightness", methods=["POST"])
def set_brightness():
    try:
        data = request.get_json()
        brightness = int(data["brightness"])
        if 0 <= brightness <= 100:
            set_led_brightness(brightness)
        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

Inside templates create a file named led_slider.html


```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LED Control</title>
    <style>
        body { font-family: Arial, sans-serif; }
        .container { max-width: 500px; margin: auto; padding: 20px; text-align: center; }
        .slider { width: 100%; margin: 20px 0; }
        h1 { margin-bottom: 20px; }
        p { font-size: 1.2em; }
    </style>
</head>
<body>
    <div class="container">
        <h1>LED Brightness Control</h1>
        <p>Adjust the brightness of the LED:</p>
        <input type="range" min="0" max="100" value="0" class="slider" id="brightnessSlider">
        <p>Brightness: <span id="brightnessValue">0</span>%</p>
    </div>
    
    <script>
        // Get references to the slider and the display span
        const slider = document.getElementById('brightnessSlider');
        const brightnessValue = document.getElementById('brightnessValue');

        // Function to update the brightness value
        slider.oninput = function() {
            brightnessValue.textContent = this.value;
            // Send the brightness value to the server
            fetch('/set_brightness', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ brightness: this.value })
            });
        };
    </script>
</body>
</html>
```
###	Access the Web Interface
Open your web browser and navigate to http://<Raspberry-Pi-IP>:5000/. For local access, use http://localhost:5000/.

### Usage

Adjust LED Brightness
  1. On the web interface, use the slider to adjust the brightness level (0-100%). The brightness value is sent to the server using AJAX each time the slider is moved.
	2.	Observe the LED
The LED will light up with the specified brightness level based on your input.
