from motor import MotorController
from sensors import SensorManager
from debug import Debugger
from errors import ErrorHandler

class Car:
    def __init__(self, debug=False):
        self.debugger = Debugger(debug)
        self.motor = MotorController()
        self.sensors = SensorManager()
        self.errors = ErrorHandler()

    def safe_drive_step(self):
        distance = self.sensors.get_distance()

        if distance is None:
            self.errors.register("Sensor liefert keine Werte.")
            self.motor.stop()
            return

        if distance < 10:
            self.debugger.log("Hindernis sehr nah – Notstopp!")
            self.motor.stop()
        else:
            self.motor.set_speed(40)
            self.debugger.log(f"Speed gesetzt: {self.motor.speed}")

    def get_state(self):
        return {
            "speed": self.motor.speed,
            "distance": self.sensors.get_distance(),
            "error": self.errors.get_last_error()
        }
