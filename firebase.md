```bash
sudo apt update
sudo apt install python3-pigpio python3-flask
sudo pip3 install firebase-admin
sudo systemctl enable pigpiod
sudo systemctl start pigpiod
```



```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LED Control</title>
    <script src="https://www.gstatic.com/firebasejs/9.0.0/firebase-app.js"></script>
    <script src="https://www.gstatic.com/firebasejs/9.0.0/firebase-database.js"></script>
    <style>
        body { font-family: Arial, sans-serif; }
        .container { max-width: 500px; margin: auto; padding: 20px; }
        .control-form { display: flex; flex-direction: column; align-items: center; }
        button { margin: 10px; padding: 10px 20px; font-size: 1.2em; cursor: pointer; }
    </style>
</head>
<body>
    <div class="container">
        <h1>LED Control</h1>
        <div class="control-form">
            <button onclick="setLEDState('on')">Turn LED On</button>
            <button onclick="setLEDState('off')">Turn LED Off</button>
        </div>
    </div>

    <script>
        // Your Firebase configuration
        // For Firebase JS SDK v7.20.0 and later, measurementId is optional
            const firebaseConfig = {
            apiKey: "gsd",
            authDomain: "g,
            databaseURL: "g",
            projectId: "g",
            storageBucket: "g",
            messagingSenderId: "g",
            appId: "g",
            measurementId: "g"
            };

        // Initialize Firebase
        const app = firebase.initializeApp(firebaseConfig);
        const db = firebase.database();

        // Function to set the LED state
        function setLEDState(state) {
            db.ref("led_state").set(state);
        }
    </script>
</body>
</html>

```


```
import time
import RPi.GPIO as GPIO
import firebase_admin
from firebase_admin import credentials, db

# Set up GPIO
LED_PIN = 18  # GPIO pin for the LED (physical pin 12)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# Function to set LED state
def set_led_state(state):
    if state.lower() == "on":
        GPIO.output(LED_PIN, GPIO.HIGH)
    else:
        GPIO.output(LED_PIN, GPIO.LOW)

# Initialize Firebase Admin SDK
cred = credentials.Certificate("firebase-adminsdk.json")  # Replace with your service account JSON file path
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://iot-test-7539f-default-rtdb.asia-southeast1.firebasedatabase.app/'  # Replace with your Firebase Realtime Database URL
})

# Reference to the LED state in the Firebase database
led_ref = db.reference('led_state')

# Function to listen for changes in the Firebase database
def listener(event):
    state = event.data
    print(f"New LED state received from Firebase: {state}")
    if state is not None:
        set_led_state(state)

# Add a Firebase listener for changes in the 'led_state' field
led_ref.listen(listener)

# Keep the program running to listen for updates
try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()

```




---

# Control an LED on a Raspberry Pi via Firebase and a Web Interface

This tutorial will guide you through controlling an LED connected to GPIO 18 of your Raspberry Pi using a Firebase database. A web interface will update the LED state (ON/OFF) in real-time by communicating with Firebase.

## Prerequisites

- A Raspberry Pi (3B or later recommended)
- An LED connected to GPIO 18 (with a resistor in series to prevent damage)
- Basic knowledge of Python and Raspberry Pi GPIO
- A Firebase account (to set up the cloud database)

## Step 1: Set Up Firebase

1. **Create a Firebase Project**:
   - Go to the [Firebase Console](https://console.firebase.google.com/) and create a new project.
   - Enable **Realtime Database** (from the left sidebar, select Realtime Database > Create Database).

2. **Add Firebase SDK for Web**:
   - After creating the project, go to **Project Settings**.
   - Under **Your apps**, find **Firebase SDK snippet** and select **Config** to get the Firebase configuration.

## Step 2: Install Required Libraries on Raspberry Pi

On your Raspberry Pi, you’ll need to install some Python libraries to interact with Firebase and control the GPIO pin:

```bash
sudo apt update
sudo apt install python3-gpiozero python3-flask
sudo pip3 install firebase-admin
```

## Step 3: Firebase Configuration for Raspberry Pi

Create a Firebase Admin SDK private key for your project:

1. Go to **Project Settings** > **Service Accounts** tab.
2. Click on **Generate new private key** to download a JSON file containing your credentials.

## Step 4: Python Script to Interface with Firebase and Control the LED

Create a Python script named `firebase_led_control.py`:

```python
import time
import gpiozero
import firebase_admin
from firebase_admin import credentials, db

# Initialize the LED on GPIO 18
LED_PIN = 18
led = gpiozero.LED(LED_PIN)

# Initialize Firebase Admin SDK
cred = credentials.Certificate("/path/to/your/firebase-adminsdk.json")  # Add your service account JSON file path
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://your-firebase-project-id.firebaseio.com'  # Replace with your Firebase Realtime Database URL
})

# Reference to the 'led_state' in the Firebase database
led_ref = db.reference('led_state')

# Function to listen for changes in the Firebase database
def listener(event):
    state = event.data
    print(f"New LED state received from Firebase: {state}")
    if state == "ON":
        led.on()
    elif state == "OFF":
        led.off()

# Add a Firebase listener for changes in the 'led_state' field
led_ref.listen(listener)

# Keep the program running to listen for updates
try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    pass

finally:
    led.off()
```

**Note**: Replace `"/path/to/your/firebase-adminsdk.json"` and `'https://your-firebase-project-id.firebaseio.com'` with your actual Firebase credentials and URL.

## Step 5: Firebase Web Interface (HTML & JavaScript)

Create a simple HTML file named `led_control.html` to control the LED state:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LED Control</title>
    <script src="https://www.gstatic.com/firebasejs/9.0.0/firebase-app.js"></script>
    <script src="https://www.gstatic.com/firebasejs/9.0.0/firebase-database.js"></script>
    <style>
        body { font-family: Arial, sans-serif; }
        .container { max-width: 500px; margin: auto; padding: 20px; text-align: center; }
        button { padding: 15px 30px; font-size: 1.5em; cursor: pointer; margin: 20px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Control the LED</h1>
        <button onclick="setLEDState('ON')">Turn ON</button>
        <button onclick="setLEDState('OFF')">Turn OFF</button>
    </div>

    <script>
        // Your Firebase configuration
        const firebaseConfig = {
            apiKey: "YOUR_API_KEY",
            authDomain: "YOUR_PROJECT_ID.firebaseapp.com",
            databaseURL: "https://YOUR_PROJECT_ID.firebaseio.com",
            projectId: "YOUR_PROJECT_ID",
            storageBucket: "YOUR_PROJECT_ID.appspot.com",
            messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
            appId: "YOUR_APP_ID"
        };

        // Initialize Firebase
        const app = firebase.initializeApp(firebaseConfig);
        const db = firebase.database();

        // Function to set LED state
        function setLEDState(state) {
            db.ref("led_state").set(state);
        }
    </script>
</body>
</html>
```

**Note**: Replace `"YOUR_API_KEY"` and other placeholders in `firebaseConfig` with your actual Firebase project details.

## Step 6: Running the Web Interface and LED Control

1. **Run the Python script on the Raspberry Pi**:
   ```bash
   sudo python3 firebase_led_control.py
   ```
2. **Open the Web Interface**:
   - You can directly open `led_control.html` in a browser.
   - Interact with the buttons to change the LED state (ON/OFF).

## Step 7: (Optional) Autostart the Firebase Listener on Boot

To run the Python script automatically on boot, create a systemd service:

1. Create a systemd service file:
   ```bash
   sudo nano /etc/systemd/system/firebase-led-control.service
   ```
2. Add the following content:
   ```ini
   [Unit]
   Description=Firebase LED Control
   After=network.target

   [Service]
   ExecStart=/usr/bin/python3 /home/pi/firebase_led_control.py
   WorkingDirectory=/home/pi
   StandardOutput=inherit
   StandardError=inherit
   Restart=always
   User=pi

   [Install]
   WantedBy=multi-user.target
   ```
3. Enable and start the service:
   ```bash
   sudo systemctl enable firebase-led-control.service
   sudo systemctl start firebase-led-control.service
   ```

## Conclusion

By integrating Firebase with your Raspberry Pi, you can control an LED from anywhere via the web. Firebase serves as the intermediary between the web interface and the Raspberry Pi, making it easy to update the LED state in real-time. This example can be adapted for other GPIO-controlled devices or IoT applications.

---



