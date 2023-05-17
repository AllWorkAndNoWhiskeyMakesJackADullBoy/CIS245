# Assignment8-1.py
# May 3rd, 2023
# Jeff Haberman
# CIS 245
# A Python script to get user input to create a virtual garage


class Vehicle:
  def setVehicle(self, VehicleMake, VehicleModel):
    self.VehicleMake = VehicleMake
    self.VehicleModel = VehicleModel
    
class Car(Vehicle):
  def setCarDoor(self, CarDoor):
    self.CarDoor = CarDoor
  def displayCarInfo(self):
    print(f"The car is a {self.VehicleMake} {self.VehicleModel} with {self.CarDoor} doors. It has been added to the garage.")

class Truck(Vehicle):
  def setBedLength(self, BedLength):
    self.BedLength = BedLength
  def displayTruckInfo(self):
    print(f"The truck is a {self.VehicleMake} {self.VehicleModel} with a bed length of {self.BedLength} inches. It has been added to the garage.")

def menu():
  print("[1]: Enter Car")
  print("[2]: Enter Truck")
  print("[3]: Exit the program")

menu()
option = int(input("Select one of these options: "))

while option != 3:
  if option == 1:
    input_CarMake = input("Please enter the car make: ")
    input_CarModel = input("Please enter the car model: ")
    input_CarDoor = input("Please enter the amount of car doors: ")
    new_car = Car()
    new_car.setVehicle(input_CarMake,input_CarModel)
    new_car.setCarDoor(input_CarDoor)
    new_car.displayCarInfo()
  elif option == 2:  
    input_TruckMake = input("Please enter the truck make: ")
    input_TruckModel = input("Please enter the truck model: ")
    input_BedLength = input("Please input the truck bed length in inches: ")
    new_truck = Truck()
    new_truck.setVehicle(input_TruckMake,input_TruckModel)
    new_truck.setBedLength(input_BedLength)
    new_truck.displayTruckInfo()
  else:
    print("You have entered an invalid selection. Try again.")
  print()
  menu()
  option = int(input("Select one of these options: "))
  