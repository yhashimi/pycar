from car import Car
import time

car = Car(debug=True)

while True:
    car.safe_drive_step()
    print(car.get_state())
    time.sleep(1)
