from components.index import pir_sensor, photoresistor, servo_motor, solenoid_relay
import utime

# Define brightness to be considered daylight. 16-bit, 0=brightest, 65536=darkest
DAYLIGHT_THRESHOLD = 20000

def press_fan_power_button():
  solenoid_relay.toggle()
  utime.sleep(0.7)
  solenoid_relay.value(0)

blinds_state = 0 # 1=open, 0=closed

# main loop
while True:
  photoresistor_value = photoresistor.read_u16()
  is_daylight = photoresistor_value < DAYLIGHT_THRESHOLD

  if is_daylight and blinds_state == 0:
    print('opening blinds')
  elif not is_daylight and blinds_state == 1:
    print('closing blinds')

  utime.sleep(0.5)