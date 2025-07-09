# Blynk + Raspberry Pi Demo (Python)

This guide walks you through controlling an LED on a Raspberry Pi using the Blynk app and Python. All steps are included: OS prep, Python environment, wiring, coding, and execution.

## Requirements

### Hardware
- Raspberry Pi (any model with internet)
- LED
- 330Ω resistor
- Breadboard and jumper wires

### Software
- Raspberry Pi OS (up to date)
- Blynk IoT app (Android or iOS)
- Python 3 (pre-installed on Raspberry Pi)

## Steps

### 1. Update Raspberry Pi

```bash
sudo apt update && sudo apt upgrade -y
```

### 2. Set Up Python Virtual Environment

```bash
sudo apt install python3-venv -y
python3 -m venv blynk_env
source blynk_env/bin/activate
```

### 3. Install Required Python Libraries

```bash
pip install blynklib RPi.GPIO
```

### 4. Connect the LED to GPIO

| Component | GPIO Pin | Physical Pin |
|-----------|----------|--------------|
| LED (+)   | GPIO17   | Pin 11       |
| LED (–)   | GND via resistor | Pin 6  |

### 5. Set Up Blynk Mobile App

1. Open the Blynk IoT app.
2. Create a new project.
3. Device: Raspberry Pi
4. Connection type: WiFi
5. Copy the Auth Token (from email or app).
6. Add a Button widget.
7. Assign it to Virtual Pin V1.
8. Set button to **Switch** mode.

### 6. Create Python Script

Create a file named `led_control.py` and paste:

```python
import blynklib
import RPi.GPIO as GPIO
import time

BLYNK_AUTH = 'YOUR_AUTH_TOKEN_HERE'

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.output(17, GPIO.LOW)

blynk = blynklib.Blynk(BLYNK_AUTH)

@blynk.handle_event('write V1')
def v1_write_handler(pin, value):
    print(f"V1 value: {value}")
    if int(value[0]) == 1:
        GPIO.output(17, GPIO.HIGH)
    else:
        GPIO.output(17, GPIO.LOW)

try:
    while True:
        blynk.run()
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Interrupted by user.")
finally:
    GPIO.cleanup()
```

Replace `YOUR_AUTH_TOKEN_HERE` with the actual token from the app.

### 7. Run the Script

```bash
source blynk_env/bin/activate
python led_control.py
```

### 8. Test the App

- Open the Blynk app.
- Tap the button.
- The LED on the Raspberry Pi should turn ON or OFF.
- The terminal will print button values.

## Exit the Script

Press `Ctrl + C` to stop. GPIO will be cleaned up automatically.

## Success

You’ve now built a full IoT demo using Raspberry Pi, Blynk, and Python!
