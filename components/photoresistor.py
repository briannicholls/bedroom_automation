from machine import ADC, Pin

class Photoresistor:
  def __init__(self, pin) -> None:
    self.control = ADC(Pin(pin))