from machine import Pin

class Button:

  def __init__(self, pin) -> None:
    self.control = Pin(pin, Pin.IN, Pin.PULL_UP)
    
  def pressed(self):
    return not self.value()

