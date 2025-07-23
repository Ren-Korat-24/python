class vehicle:
    def start_engine(self):
        print("Engine started")

class Car(vehicle):
    def car_drive(self):
        print("Car is start")

c= Car()
c.start_engine()
c.car_drive()