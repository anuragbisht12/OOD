"""
Design Parking Lot
"""
from abc import ABCMeta,abstractmethod

from enum import Enum
class VehicleSize(Enum):
    LARGE=3
    COMPACT=2
    MOTORCYCLE=1


class  Vehicle(metaclass=ABCMeta):
    _parkingSpots=[[]]
    _spotNeeded=None
    _vehicleSize=None

    def getSpotsNeeded(self):
        return self._spotNeeded
    
    def getSize(self):
        return self._vehicleSize

    def parkingSpot(self,s):
        self._parkingSpots.append(s)

    def clearSpots(self):
        pass

    @abstractmethod
    def canFitinSpot(self,spot):
        pass


class Bus(Vehicle):

    def __init__(self):
        self._spotNeeded = 5
        self._vehicleSize = VehicleSize.LARGE

    def canFitinSpot(self, spot):
        pass

    
class Car(Vehicle):

    def __init__(self):
        self._spotNeeded=2
        self._vehicleSize=VehicleSize.COMPACT

    def canFitinSpot(self, spot):
        pass


class Motorcycle(Vehicle):

    def __init__(self):
        self._spotNeeded=1
        self._vehicleSize=VehicleSize.MOTORCYCLE

    def canFitinSpot(self, spot):
        pass



