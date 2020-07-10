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

#my parent class
class Vehicle():
    def __init__(self, name):
        self.name = name

class GroundVehicle(Vehicle):
    def __init__(self, name, make):
        super().__init__(name)
        self.make = make

class Car(GroundVehicle):
    def __init__(self, name, make):
        super().__init__(name, make)

class Motorcycle(GroundVehicle):
    def __init__(self, name, make):
        super().__init__(name, make)


class FlightVehicle():
    def __init__(self):
        super().__init__()

class Airplane(FlightVehicle):
    def __init__(self):
        super().__init__()

class Starship():
    def __init__(self):
        super().__init__()