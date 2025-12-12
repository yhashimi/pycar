class MotorController:
    def __init__(self):
        self.speed = 0

    def set_speed(self, value):
        # Sicherheitslimit
        value = max(0, min(100, value))
        self.speed = value

    def stop(self):
        self.speed = 0
