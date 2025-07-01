
# Raspberry Pi LED Blink with Python

This project demonstrates how to blink an LED using Python on a Raspberry Pi 3B with the `gpiozero` library.

## 🧰 What You Need

- Raspberry Pi 3B (with Raspbian OS installed)
- 1x LED
- 1x 220Ω resistor (or similar)
- Breadboard and jumper wires
- Internet connection (for installing libraries if needed)

## 📌 Wiring Instructions

| LED Leg       | Connect To                  |
|---------------|-----------------------------|
| Longer (Anode) | Physical Pin 11 (GPIO 17)   |
| Shorter (Cathode) | Resistor → GND (e.g., Pin 6) |

> 💡 GPIO 17 corresponds to **physical pin 11** on the Raspberry Pi 3B.
>![Pin Layout](https://raw.githubusercontent.com/bitstudens/IoT-practicals/main/pin_layout.png)
>![Design](https://raw.githubusercontent.com/bitstudens/IoT-practicals/main/design.jpeg)
> 

### Pin Reference

| Physical Pin | BCM GPIO | Description |
|--------------|-----------|-------------|
| 11           | GPIO 17   | Output to LED |
| 6            | GND       | Ground        |

---

## 🧪 Python Code

Save the following code in a file named `blink.py`:

```python
from gpiozero import LED
from time import sleep

led = LED(17)  # BCM GPIO 17 (physical pin 11)

while True:
    led.toggle()
    print("LED is ON" if led.value else "LED is OFF")
    sleep(1)


---

▶️ Running the Program

1. Open a terminal on your Raspberry Pi.


2. Navigate to the folder containing blink.py.


3. Run the script:



python3 blink.py

Press Ctrl+C to stop the program.


---

