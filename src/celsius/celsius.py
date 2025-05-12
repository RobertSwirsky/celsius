from w1thermsensor import W1ThermSensor, Unit
import RPi.GPIO as GPIO
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

class sensor:
    def __init__(self, sensor_list):
        GPIO.setmode(GPIO.BCM)
        self.sensor_list = sensor_list
        self.initialize_soft_pullups()

    def initialize_soft_pullups(self):
        for p in self.sensor_list:
            pass
        
        
    def print_temperatures(self):
        for sensor in W1ThermSensor.get_available_sensors():
            print("Sensor %s has temperature %.2f" % (sensor.id, sensor.get_temperature()))

    def get_sensor_list(self):
        return W1ThermSensor.get_available_sensors()



