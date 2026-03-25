class vehicle():
    def start(self):
        pass

    def stop(self):
        print("vehicle stopped")

    def fuel_type(self):
        print("General fuel")

class Car(vehicle):
    def start(self):
        print("Car starts with key or button")

class bike(vehicle):
    def start(self):
        print("Bike starts with kick or self-start")

class Truck(vehicle):
    def start(self):
        print("Truck starts with heavy ignition system")


vehicle =[bike(),Car(),Truck()]

for v in vehicle:
    v.start()