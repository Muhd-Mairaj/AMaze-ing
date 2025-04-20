import RPi.GPIO as GPIO
import time
class MyServo:
  def __init__(self, input_pin: int):
    """
    Class to control a servo motor.

    Args:
        input_pin (int): GPIO pin connected to the servo signal wire.
    """
    self.input_pin = input_pin
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.input_pin, GPIO.OUT)
    self.pwm = GPIO.PWM(self.input_pin, 50)  # 50Hz for standard servo
    self.pwm.start(0)

  def move_servo(self, angle: int):
    """
    Function Name: move_servo
    Params:
        angle (int or float): Desired angle to rotate the servo (0 to 180).
    Returns:
        None
    """
    # Clamp angle between 0 and 180
    angle = max(0, min(180, angle))

    # Map angle to duty cycle (2% to 12%)
    duty = 2 + (angle / 18)

    self.pwm.ChangeDutyCycle(duty)
    time.sleep(0.5)

    self.pwm.ChangeDutyCycle(0)  # Stop sending signal to hold position

  def cleanup(self):
    """
    Function Name: cleanup
    Clean up GPIO settings.
    """
    self.pwm.stop()
    GPIO.cleanup()