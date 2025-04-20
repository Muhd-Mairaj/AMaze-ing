import RPi.GPIO as GPIO

# Setup function — should be called once before using IRSensor
def setup_sensor(sensorPin):
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(sensorPin, GPIO.IN)

# Main function
def IRSensor(sensorPin):
  """
  Function Name: IRSensor
  Params:
      sensorPin (int): The GPIO pin number connected to the IR sensor.
  Returns:
      bool: True if stop, False otherwise.
  """
  sensorStatus = GPIO.input(sensorPin)

  if sensorStatus == 1:
    return True  # Stop
  else:
    return False  # Continue

def test_main():
  setup_sensor(9)
  while True:
    sensor = IRSensor(9)