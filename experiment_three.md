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
--pip install blynklib RPi.GPIO
pip3 install RPi.GPIO
pip3 install blynk-library-python
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
import BlynkLib
import time
import RPi.GPIO as GPIO

# Replace with your own Blynk Auth Token
BLYNK_AUTH = 'YourAuthTokenHere'

# Setup GPIO
LED_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# Connect to the Blynk 2.0 server using non-SSL (port 80)
blynk = BlynkLib.Blynk(BLYNK_AUTH, server="blynk.cloud", port=80)

# Handle virtual pin V0 writes from the Blynk app
@blynk.VIRTUAL_WRITE(0)
def v0_write_handler(value):
    print(f"Received value from V0: {value}")
    GPIO.output(LED_PIN, int(value[0]))

print("Connecting to Blynk Cloud...")
try:
    while True:
        blynk.run()
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nExiting. Cleaning up GPIO...")
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
