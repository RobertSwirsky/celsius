
import RPi.GPIO as GPIO
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import sys

class sensor:
    def __init__(self, sensor_list):
        GPIO.setmode(GPIO.BCM)
        self.sensor_list = sensor_list
        self.check_kernel_modules()

    def is_kernel_module_loaded(self, module_name):
        with open('/proc/modules', 'r') as f:
            modules = f.read()
        return module_name in modules
    
    def check_kernel_modules(self):
        # from w1thermsensor import W1ThermSensor, Unit
        required_modules = ['w1_gpio', 'w1_therm']
        missing = [m for m in required_modules if not self.is_kernel_module_loaded(m)]

        if missing:
            print(f"Missing required kernel modules: {', '.join(missing)}. Please see readme about config.txt file.")
            return False
        else:
            return True

        
    def print_temperatures(self):
        from w1thermsensor import W1ThermSensor, Unit
        for sensor in W1ThermSensor.get_available_sensors():
            print("Sensor %s has temperature %.2f" % (sensor.id, sensor.get_temperature()))

    def get_sensor_list(self):
        from w1thermsensor import W1ThermSensor, Unit
        return W1ThermSensor.get_available_sensors()



