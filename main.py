from car import Car
import time

car = Car(debug=True)

try:
    while True:
        car.safe_drive_step()
        print(car.get_state())
        time.sleep(1)
except KeyboardInterrupt:
        car.px.forward(0)
        car.motor.stop()
        print("Programm beendet")
