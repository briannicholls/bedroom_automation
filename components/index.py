from machine import Pin
from servo import Servo
from photoresistor import Photoresistor
from button import Button
from switch import Switch

###########
# Sensors #
###########

pir_sensor     = Pin(16, Pin.IN)
photoresistor  = Photoresistor(26)

##############
# Mechanical #
##############

solenoid_relay = Pin(15, Pin.OUT)
servo_motor    = Servo(18)

########################
# Buttons and Switches #
########################

# Toggle switch for blinds automation
daylight_check_switch = Switch(1)

# Button to press to turn on fan
fan_power_button    = Button(2)

# Manual blinds buttons
blinds_open_button  = Button(3)
blinds_close_button = Button(4)
