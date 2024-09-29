# Blynk Setup on Raspberry Pi

## Prerequisites
Before you begin, make sure you have:
- A Raspberry Pi with Raspberry Pi OS installed.
- An active internet connection.
- The Blynk app installed on your smartphone (available on iOS and Android) with an active Blynk account.

## 1. Download and Extract the Blynk Library

1. **Download the Blynk Library:**
   - Go to the [Blynk Library GitHub Repository](https://github.com/vshymanskyy/blynk-library-python).
   - Click on the **Code** button and select **Download ZIP** to download the library to your local machine.

2. **Extract the Library:**
   - Extract the downloaded ZIP file. If using the terminal on your Raspberry Pi, navigate to the directory where you downloaded the file and run:
     ```bash
     unzip blynk-library-python-master.zip
     ```
   - This will create a directory named `blynk-library-python-master` containing the extracted files.

## 2. Install Dependencies

1. **Update System Packages:**
   - Ensure your system packages are up-to-date:
     ```bash
     sudo apt-get update
     ```

2. **Install Required Packages:**
   - Install `python3-pip` if it's not already installed:
     ```bash
     sudo apt-get install python3-pip
     ```

## 3. Set Up Blynk on Raspberry Pi

1. **Create a New Project in the Blynk App:**
   - Open the Blynk app on your smartphone.
   - Create a new project and select **Raspberry Pi** as the device type.
   - Choose the **Connection Type** (e.g., WiFi).

2. **Add Widgets and Configure Datastreams:**
   - Add widgets such as a Button to control your LED.
   - Configure the datastreams for these widgets.

3. **Obtain Your Auth Token:**
   - After configuring your project, the Blynk app will provide an **Auth Token**. Copy this token as you will need it for your code.

## 4. Update Auth Token in Your Code

1. **Insert the Auth Token:**
   - In your Python script, replace the placeholder for the Auth Token with the one you copied from the Blynk app.

## Additional Resources

- For detailed instructions and troubleshooting, refer to the [Blynk Documentation](https://docs.blynk.io/) or visit the [Blynk Community](https://community.blynk.cc/).




### Create Python Virtual Enviroment
```
python -m venv env
source env/bin/activate
pip install Blynk

```

### Code

```
import BlynkLib
import RPi.GPIO as GPIO
import BlynkTimer

BLYNK_AUTH_TOKEN = 'r0qBQnVShdvwsY4PLtDPLV3jv6iwrpgt' #Update this with your auth token

led1 = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led1, GPIO.OUT)


x = 20
# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH_TOKEN)

# Led control through V0 virtual pin
@blynk.on("V0")
def v0_write_handler(value):
#    global led_switch
    if int(value[0]) is not 0:
        GPIO.output(led1, GPIO.HIGH)
        print('LED1 HIGH')
    else:
        GPIO.output(led1, GPIO.LOW)
        print('LED1 LOW')

#function to sync the data from virtual pins
@blynk.on("connected")
def blynk_connected():
    print("Raspberry Pi Connected to New Blynk") 

while True:
    blynk.run()
```


