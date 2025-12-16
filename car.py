import time
from picarx import Picarx
from motor import MotorController
from sensor import SensorManager
from debug import Debugger
from error import ErrorHandler

SAFE_DISTANCE = 40
DANGER_DISTANCE = 25
POWER = 50

class Car:
    def __init__(self, debug=False):
        self.debugger = Debugger(debug)
        self.motor = MotorController()
        self.sensor = SensorManager()
        self.error = ErrorHandler()
        self.steering_angle = 0
        # PicarX-Objekt für direkte Steuerung
        self.px = Picarx()

    def safe_drive_step(self):
        try:
            distance = round(self.px.ultrasonic.read(), 2)
            self.debugger.log(f"Distance: {distance} cm")
        except:
            self.px.stop()
            return

        if distance >= SAFE_DISTANCE:
            self.px.set_dir_servo_angle(0)
            self.px.forward(POWER)

        elif distance >= DANGER_DISTANCE:
            self.px.stop()
            time.sleep(0.05)
            self.px.set_dir_servo_angle(30)
            self.px.forward(20)

        else:
            self.px.stop()
            time.sleep(0)
            self.px.set_dir_servo_angle(-30)
            self.px.backward(POWER)
            time.sleep(1)
            self.px.stop()

    def get_state(self):
        return {
            "speed": self.motor.speed,
            "distance": self.sensor.get_distance(),
            "steering_angle": self.steering_angle,
            "error": self.error.get_last_error()
        }
