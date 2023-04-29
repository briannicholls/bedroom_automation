from machine import ADC, Pin
import utime
import _thread

INTERVAL = 10 * 60  # 10 minutes

class Photoresistor:
  def __init__(self, pin) -> None:
    self.control = ADC(Pin(pin))
    self.is_checking_daylight = False
    self.servo = None # servo to control
    self.blinds_state = 0 # 0 = closed, 1 = open

  def read_value(self):
    return self.control.read_u16()
  
  def check_daylight(self, daylight_threshold):
    photoresistor_value = self.read_value()
    is_daylight = photoresistor_value < daylight_threshold

    if is_daylight and self.blinds_state == 0:
      self.servo.open_blinds()
      self.blinds_state = 1
    elif not is_daylight and self.blinds_state == 1:
      self.servo.close_blinds()
      self.blinds_state = 0

  def _daylight_loop(self, daylight_threshold):
    while self.is_checking_daylight:
      self.check_daylight(daylight_threshold)
      utime.sleep(INTERVAL)

  # Starts a separate thread to check for daylight,
  # and trigger given servo to open/close blinds
  def start_checking_daylight(self, daylight_threshold, servo):
    self.is_checking_daylight = True
    self.servo = servo
    _thread.start_new_thread(self._daylight_loop, (daylight_threshold))

  # Stops the thread that checks for daylight
  def stop_checking_daylight(self):
    print('stopping daylight check')
    self.is_checking_daylight = False