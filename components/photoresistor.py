from machine import ADC, Pin
import utime
import _thread

class Photoresistor:
  def __init__(self, pin) -> None:
    self.control = ADC(Pin(pin))
    self.is_checking_daylight = False

  def read_value(self):
    return self.control.read_u16()
  
  def check_daylight(self, daylight_threshold, blinds_state):
    photoresistor_value = self.read_value()
    is_daylight = photoresistor_value < daylight_threshold

    if is_daylight and blinds_state == 0:
        print('opening blinds')
    elif not is_daylight and blinds_state == 1:
        print('closing blinds')

  def _daylight_loop(self, daylight_threshold, blinds_state):
      while self.is_checking_daylight:
          self.check_daylight(daylight_threshold, blinds_state)
          utime.sleep(10 * 60)  # Sleep for 10 minutes

  def start_checking_daylight(self, daylight_threshold, blinds_state):
      print('starting daylight check')
      self.is_checking_daylight = True
      _thread.start_new_thread(self._daylight_loop, (daylight_threshold, blinds_state))

  def stop_checking_daylight(self):
      print('stopping daylight check')
      self.is_checking_daylight = False