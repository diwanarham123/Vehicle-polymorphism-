class BMW:
    def fuel_type(self):
        print("Diesel/Petrol")

    def max_speed(self):
        print("250 km/h")

class Ferrari:
    def fuel_type(self):
        print("Petrol")

    def max_speed(self):
        print("320 km/h")

bmw_car = BMW()
ferrari_car = Ferrari()

for car in (bmw_car, ferrari_car):
    car.fuel_type()
    car.max_speed()
   