class Vehicle:
   company = "XYZ Motors"

   def __init__(self, n_wheels, n_seats, mileage):
      print("init of Vehicle")
      self.n_wheels = n_wheels
      self.n_seats = n_seats
      self.mileage = mileage

   def get_details(self):
      return f"This vehicle has {self.n_wheels} wheels, {self.n_seats} seats and provide a mileage of{self.mileage}"   



class Car(Vehicle):
   model = "ABC123"
   def __init__(self, car_type, drive_type, wheels, seats, mileage):
      print("init of Car")
      self.car_type = car_type
      self.drive_type = drive_type
      # Vehicle.__init__(self,4, 7, 20)
      super().__init__(wheels, seats, mileage)

   def display_info(self):
      print(f"Car type: {self.car_type}, Drive type: {self.drive_type}")   



class ElectricCar(Car):
   def __init__(self, car_type, drive_type, wheels, seats, mileage, battery_capacity, distance_range):
      print("init of ElectricCar")
      self.battery_capacity = battery_capacity
      self.distance_range = distance_range
      super().__init__(car_type, drive_type, wheels, seats, mileage)


   def charge(self):
      print(f"Chargin the to {self.battery_capacity}")   


ec1 = ElectricCar("Sedan", "Manual", 4, 5, 35, 100, 400)   

print(ec1.__dict__)

help(ElectricCar)