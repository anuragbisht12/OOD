# Behavioral pattern
# Abstract Class: declares interface to define the steps of the algorithm
# Concrete Class: this defines subclass specific step definition
# template method(): This defines the algorithm by calling the steps methods

from abc import ABCMeta, abstractmethod


class Trip(metaclass=ABCMeta):
    """ abstract class"""
    @abstractmethod
    def setTransport(self):
        pass

    @abstractmethod
    def day1(self):
        pass
    
    @abstractmethod
    def day2(self):
        pass

    @abstractmethod
    def day3(self):
        pass

    @abstractmethod
    def returnHome(self):
        pass
    
    def itinerary(self):
        self.setTransport()
        self.day1()
        self.day2()
        self.day3()
        self.returnHome()


class VeniceTrip(Trip):
    """Concrete class"""

    def setTransport(self):
        print("Take a boat and find your way in the grand canal")

    def day1(self):
        print("Visit St Mark in St Mark Square")
    
    def day2(self):
        print("Appreciate Dog's palace")

    def day3(self):
        print("Enjoy the food near the Bridge")     
    
    def returnHome(self):
        print("Get souvenirs for friends and get back")


class MaldivesTrip(Trip):
    """Concrete class"""

    def setTransport(self):
        print("On foot on any island")

    def day1(self):
        print("Enjoy the marine life of banana reef")

    def day2(self):
        print("Go for the water sports")

    def day3(self):
        print("Relax on the beach and enjoy the sun")

    def returnHome(self):
        print("Dont feel like leaving the beach")


class TravelAgency:
    def arrangeTrips(self):
        choice = input("What kind of place historical or beach ? ")
        if choice == "historical":
            self.trip=VeniceTrip()
            self.trip.itinerary()
        
        if choice == 'beach':
            self.trip= MaldivesTrip()
            self.trip.itinerary()

if __name__ == "__main__":
    TravelAgency().arrangeTrips()


# hooks: give subclass ability to hook into the algorithm whenever needed
# moulding the exisitng functionality like changeing the day 2 plan

# Hollywood design principle: Dont call us, we will call you
# Production houses call actors if there is any rol for the actors

# advantages:code reuse
# disadvantages: maintenance

