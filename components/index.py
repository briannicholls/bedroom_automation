from machine import Pin
from servo import Servo
from photoresistor import Photoresistor

solenoid_relay = Pin(15, Pin.OUT)
pir_sensor     = Pin(16, Pin.IN)
photoresistor  = Photoresistor(26)
servo_motor    = Servo(18)
