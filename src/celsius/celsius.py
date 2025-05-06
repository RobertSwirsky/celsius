from w1thermsensor import W1ThermSensor, Unit
import RPi.GPIO as GPIO
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

def initialize_soft_pullups(pullups):
    for p in pullups:
        GPIO.setup(p, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
def print_temperatures():
    for sensor in W1ThermSensor.get_available_sensors():
        print("Sensor %s has temperature %.2f" % (sensor.id, sensor.get_temperature())

if __name__== "__main__":
    print("main")
    GPIO.setmode(GPIO.BCM)
    sensor_list = [4]
    initialize_soft_pullups(sensor_list)
    print_temperatures()
