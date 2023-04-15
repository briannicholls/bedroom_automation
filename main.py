# Import all hardware components
from components.index import (
  photoresistor,
  solenoid_relay,
  daylight_check_switch,
  fan_power_button,
  servo_motor,
  pir_sensor,
  blinds_open_button,
  blinds_close_button
)

import utime

# Define brightness to be considered daylight. 16-bit, 0=brightest, 65536=darkest
DAYLIGHT_THRESHOLD = 20000

def activate_solenoid():
  solenoid_relay.value(1)
  utime.sleep(0.5)
  solenoid_relay.value(0)

# Check if user is pressing the fan power button
def is_fan_power_button_pressed():
  return not fan_power_button.value()

blinds_state = 0 # 1=open, 0=closed

# main loop
while True:

  # Check if user disabled daylight checking
  if photoresistor.is_checking_daylight and not(daylight_check_switch):
    photoresistor.stop_checking_daylight()
  elif not(photoresistor.is_checking_daylight) and daylight_check_switch:
    photoresistor.start_checking_daylight()

  # Check if user is pressing the fan power button
  if is_fan_power_button_pressed():
    activate_solenoid()

    # Debounce the button press
    while is_fan_power_button_pressed():
      utime.sleep(0.2)


  # Check if user is pressing the blinds button
  
  