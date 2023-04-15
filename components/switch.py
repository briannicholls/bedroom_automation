from machine import Pin

class Switch:

  def __init__(self, pin) -> None:
    self.control = Pin(pin, Pin.IN, Pin.PULL_UP)
    
  def value(self):
    return self.control.value()