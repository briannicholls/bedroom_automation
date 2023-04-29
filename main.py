import utime
from constants import *

# Import all hardware components
from components.index import (
    photoresistor,
    solenoid_relay,
    daylight_check_switch,
    fan_power_button,
    servo_motor,
    pir_sensor,
    blinds_open_button,
    blinds_close_button,
)


# Solenoid sequence for pressing the fan power button
def activate_solenoid():
    solenoid_relay.value(1)
    utime.sleep(0.5)
    solenoid_relay.value(0)

###############
# Main Program
###############

# Set up triggers for all switches and buttons

# Manual fan button - activate solenoid on press
fan_power_button.set_on_press_callback(activate_solenoid)

# Manual blinds buttons - open/close blinds on press, stop on release
blinds_open_button.set_on_press_callback(servo_motor.open)
blinds_close_button.set_on_press_callback(servo_motor.close)
blinds_open_button.set_on_release_callback(servo_motor.stop)
blinds_close_button.set_on_release_callback(servo_motor.stop)

# Photoresistor daylight check switch - start/stop checking daylight on switch
daylight_check_switch.set_on_callback(
    lambda: photoresistor.start_checking_daylight(
        DAYLIGHT_THRESHOLD, servo_motor
    )
)
daylight_check_switch.set_off_callback(photoresistor.stop_checking_daylight)
