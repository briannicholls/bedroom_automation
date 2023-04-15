from machine import PWM, Pin
import utime
class Servo:

  # initialize with GPIO pin
  def __init__(self, pin) -> None:
    self.control = PWM(Pin(pin))
    self.control.freq(50) # Set PWM frequency to 50Hz

  # accepts desired pulse width in microseconds
  def set_pulse_width(self, pulse_width_us):
    # divide the scaled pulse width (16bit) by the total period
    # 1 / 50 Hz = 0.02 seconds = 20,000 µs
    duty_cycle = (pulse_width_us * 65535) // 20000
    self.control.duty_u16(duty_cycle)

  # Stop rotation
  def stop(self): 
    self.set_pulse_width(1500)
    
  # Rotate clockwise
  def open(self):
    self.set_pulse_width(2000)

  # Rotate counter-clockwise
  def close(self):
    self.set_pulse_width(1000)

  def open_blinds(self):
    print('opening blinds')
    self.open()
    utime.sleep(2)
    self.stop()

  def close_blinds():
    print('closing blinds')
    self.close()
    utime.sleep(2)
    self.stop()
