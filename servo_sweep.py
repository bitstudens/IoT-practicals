from gpiozero import AngularServo
from time import sleep

# Physical pin 11 is BCM GPIO17.
SERVO_GPIO = 17

# Change these values if your servo needs calibration.
MIN_PULSE_WIDTH = 0.0005
MAX_PULSE_WIDTH = 0.0025

# The servo will move through these target angles and then return.
TARGET_ANGLES = [30, 60, 90, 120, 150, 120, 90, 60, 30]

# Delay between one-degree movements.
# Increase this value for slower movement.
STEP_DELAY_SECONDS = 0.02

# Pause after reaching each target angle.
TARGET_PAUSE_SECONDS = 0.5


servo = AngularServo(
    SERVO_GPIO,
    min_angle=0,
    max_angle=180,
    min_pulse_width=MIN_PULSE_WIDTH,
    max_pulse_width=MAX_PULSE_WIDTH,
    initial_angle=None,
)


def move_smoothly(current_angle: int, target_angle: int) -> int:
    """Move the servo one degree at a time toward the target angle."""
    if current_angle < target_angle:
        step = 1
    else:
        step = -1

    for angle in range(current_angle, target_angle, step):
        servo.angle = angle
        sleep(STEP_DELAY_SECONDS)

    servo.angle = target_angle
    return target_angle


try:
    current_angle = 30
    servo.angle = current_angle
    sleep(1)

    print("Servo sweep started. Press Ctrl+C to stop.")

    while True:
        for target_angle in TARGET_ANGLES:
            print(f"Moving to {target_angle} degrees")
            current_angle = move_smoothly(current_angle, target_angle)
            sleep(TARGET_PAUSE_SECONDS)

except KeyboardInterrupt:
    print("\nServo sweep stopped.")

finally:
    servo.detach()
