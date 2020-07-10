# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

#my parent class to groundvehicle.
class Vehicle():
    pass

class GroundVehicle(Vehicle): #parent to car and motorcycle
    pass

class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass

class FlightVehicle(Vehicle): #parent to airplane
    pass

class Airplane(FlightVehicle):
    pass

class Starship(FlightVehicle):
    pass
