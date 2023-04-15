from machine import Pin
import utime

class Button:

  def __init__(self, pin) -> None:
    self.control = Pin(pin, Pin.IN, Pin.PULL_UP)
    
  def pressed(self):
    return not self.value()

  # when button is pressed, run callback function (0.2s debounce)
  def on_press(self, on_press_callback):
    while True:
      if self.pressed():
        on_press_callback()

        # Debounce the button press
        while self.pressed():
          utime.sleep(0.2)
