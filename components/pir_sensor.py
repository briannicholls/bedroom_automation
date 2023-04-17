from machine import Pin
import utime

class PIRSensor:

  def __init__(self, pin, on_motion=None, on_no_motion=None) -> None:
    self.control = Pin(pin, Pin.IN)
    self._on_motion = on_motion
    self._on_no_motion = on_no_motion
    self.last_motion_timestamp = None
    self.control.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=self._handle_event)

  def _handle_event(self, pin):
    if pin.value():  # Rising edge (motion detected)
      if self._on_motion:
        self._on_motion()
    else:  # Falling edge (no motion detected)
      if self._on_no_motion:
        self._on_no_motion()

  def value(self):
    return self.control.value()

  def set_on_motion_callback(self, on_motion):
    self._on_motion = on_motion

  def set_on_no_motion_callback(self, on_no_motion):
    self._on_no_motion = on_no_motion

  def time_since_last_motion(self):
    if self.last_motion_timestamp is None:
      return None
    return utime.time() - self.last_motion_timestamp