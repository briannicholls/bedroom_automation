from machine import Pin
import utime

class Button:
  def __init__(self, pin, on_press=None, on_release=None) -> None:
    self.control = Pin(pin, Pin.IN, Pin.PULL_UP)
    self._on_press = on_press
    self._on_release = on_release
    self.control.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=self._handle_event)

  def _handle_event(self, pin):
    if pin.value():  # Rising edge (button released)
      if self._on_release:
        self._on_release()
    else:  # Falling edge (button pressed)
      if self._on_press:
        self._on_press()

  def pressed(self):
    return not self.control.value()

  def set_on_press_callback(self, on_press):
    self._on_press = on_press

  def set_on_release_callback(self, on_release):
    self._on_release = on_release
