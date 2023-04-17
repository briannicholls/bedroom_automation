from machine import Pin

class Switch:
  def __init__(self, pin, on_on=None, on_off=None) -> None:
    self.control = Pin(pin, Pin.IN, Pin.PULL_UP)
    self._on_on = on_on
    self._on_off = on_off
    self.control.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=self._handle_event)

  def _handle_event(self, pin):
    if pin.value():  # Rising edge (switch turned off)
      if self._on_off:
        self._on_off()
    else:  # Falling edge (switch turned on)
      if self._on_on:
        self._on_on()

  def value(self):
    return self.control.value()

  def set_on_callback(self, on_on):
    self._on_on = on_on

  def set_off_callback(self, on_off):
    self._on_off = on_off
