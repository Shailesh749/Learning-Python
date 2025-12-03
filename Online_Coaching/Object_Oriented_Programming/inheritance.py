class Vehicle:
   company = "XYZ Motors"

   def __init__(self, n_wheels, n_seats, mileage):
      print("init of Vehicle")
      self.n_wheels = n_wheels
      self.n_seats = n_seats
      self.mileage = mileage

   def get_details(self):
      return f"This vehicle has {self.n_wheels} wheels, {self.n_seats} seats and provide a mileage of{self.mileage}"   
      

# v1 = Vehicle(4, 7, 40)
# print(v1.get_details())  



class Car(Vehicle):
   model = "ABC123"
   def __init__(self, car_type, drive_type, wheels, seats, mileage):
      print("init of Car")
      self.car_type = car_type
      self.drive_type = drive_type
      # Vehicle.__init__(self,4, 7, 20)
      super().__init__(wheels, seats, mileage)

# Car class inherits the Vehicle class
# Car class is called Child class/derived class
# Vehicle class is called Parent class/base class


# c1 = Car(4, 5, 30)
# print(c1)

# help(Car)
# print(c1.mileage)
# print(c1.company)
# print(c1.get_details())



c1 = Car("SUV", "Manual", 4, 7, 20)
# print(c1)
# help(Car)
print(c1.model)
print(c1.company)
print(c1.company)
print(c1.mileage)
print(c1.get_details())
print(c1.__dict__)