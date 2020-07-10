# Structural design pattern
# structural patterns describe how objects and classes can be combined to form larger structures.
# Facade hides complexities between client and subsystem acting as interface

class EventManager(object):
    """Facade class acting as interface between client and subsystem"""
    def __init__(self):
        print("Event manager :: Let me talk to the folks")
    def arrange(self):
        self.hotelier=Hotelier()
        self.hotelier.bookHotel()

        self.florist=Florist()
        self.florist.setFlowerRequirements()

        self.caterer=Caterer()
        self.caterer.setCuisine()

        self.musician=Musician()
        self.musician.setMusicType()


class Hotelier(object):
    """Subsystems"""
    def __init__(self):
        print("Arranging the Hotel for Marriage? ")
    
    def _isAvailable(self):
        print("Is the hotel free for the event for on a given day? ")
        return True
    
    def bookHotel(self):
        if self._isAvailable():
            print("Registered the booking")

class Florist(object):
    def  __init__(self):
        print("Flower decorations for the event ?")

    def setFlowerRequirements(self):
        print("Roses and lilies will be used.")


class Caterer(object):
    def __init__(self):
        print("Food arrangements for the event? ")
    
    def setCuisine(self):
        print("Chinese and Continental Cuisine to be served. ")

class Musician(object):
    def __init__(self):
        print("Musical arrangements for the marriage? ")
    
    def setMusicType(self):
        print("Jazz and classical will be played")


class You(object):
    def __init__(self):
        print("You : Whoa Marriage arrangements?")

    def askEventManager(self):
        print("You: Lets connect to the event manager")
        em=EventManager()
        em.arrange()

    def __del__(self):
        print("You : Thanks to the event manager, all preparations done. ")

if __name__ == "__main__":
    you=You()
    you.askEventManager()

# principle of least knowledge
# Also called as law of demeter
# 1. a unit should have limited knowldege of other units
# 2. A unit should talk to its friends only
# 3. A unit should not know internal implementation details of object that it manipulates

# disadvantages: if there are multiple unnecessary interfaces, it can lead to performance issues
