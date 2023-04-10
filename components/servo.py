from machine import PWM, Pin

class Servo:

  # initialize with machine.PWM
  def __init__(self, pin) -> None:
    self.control = PWM(Pin(pin))
    self.control.freq(50) # Set PWM frequency to 50Hz

  def open_blinds(self):
    