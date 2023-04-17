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

blinds_state = 0 # 1=open, 0=closed

# Set the on_press callback for the manual fan button
fan_power_button.set_on_press_callback(activate_solenoid)

# Set the on_press / on_release callbacks for the manual blinds buttons
blinds_open_button.set_on_press_callback(servo_motor.open())
blinds_close_button.set_on_press_callback(servo_motor.close())
blinds_open_button.set_on_release_callback(servo_motor.stop())
blinds_close_button.set_on_release_callback(servo_motor.stop())


# main loop
while True:
  utime.sleep(1)

  # Check if user disabled daylight checking, otherwise begin checking
  if photoresistor.is_checking_daylight and not(daylight_check_switch):
    photoresistor.stop_checking_daylight()
  elif not(photoresistor.is_checking_daylight) and daylight_check_switch:
    photoresistor.start_checking_daylight(DAYLIGHT_THRESHOLD, blinds_state, servo_motor)

