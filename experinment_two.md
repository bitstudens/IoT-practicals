# 🧠 IoT LED Control Using MQTT and Raspberry Pi (All-in-One Guide)

This guide will help you wire an LED, install necessary tools, write an MQTT listener script, and test it using `mosquitto_pub`.

---

## 🔌 1. Wiring the LED

**Connect like this:**

```
GPIO17 (Pin 11) ---> Resistor ---> Long leg of LED (anode)
Short leg of LED (cathode) ---> GND (Pin 6)
```

---

## 🛠️ 2. Install Dependencies on Raspberry Pi

```bash
sudo apt update
sudo apt install python3-gpiozero mosquitto-clients -y
pip install paho-mqtt
```

---

## 📝 3. Create the MQTT LED Control Script

Create and open the file:

```bash
nano led_mqtt.py
```

Paste this code:

```python
import paho.mqtt.client as mqtt
from gpiozero import LED

led = LED(17)  # GPIO17

def on_connect(client, userdata, flags, rc):
    print("Connected with result code", rc)
    client.subscribe("iot/led")

def on_message(client, userdata, msg):
    command = msg.payload.decode().lower()
    print(f"Received: {command}")
    
    if command == "on":
        led.on()
    elif command == "off":
        led.off()
    else:
        print("Unknown command")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("broker.hivemq.com", 1883, 60)
client.loop_forever()
```

Save and exit:
- Press `Ctrl + X`, then `Y`, then `Enter`

---

## ▶️ 4. Run the Script

```bash
python3 led_mqtt.py
```

Keep this terminal open — it listens for MQTT commands.

---

## 🧪 5. Test the LED via MQTT

### Open a new SSH terminal/tab and connect again:(Optional)

```bash
ssh bit@raspberrypi.local
```

### Then send commands:

```bash
# Turn LED ON
mosquitto_pub -h broker.hivemq.com -t iot/led -m "on"

# Turn LED OFF
mosquitto_pub -h broker.hivemq.com -t iot/led -m "off"
```

---

## ✅ Behavior

- `"on"` → LED turns ON
- `"off"` → LED turns OFF

If the behavior is inverted, check that the **long leg of the LED is connected to GPIO17 through the resistor**, and the **short leg is to GND**.
