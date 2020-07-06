# Behavioral Design pattern
# State patterns allow object to change its behavior when its internal state changes
# The state design pattern is used to develop Finite State machines

# Participants
# 1. State: Interface that defines the Handle() abstract method. The Handle() method needs to be implemented by ConcreteState
# 2. ConcreteState: these implements the Handle() method and define the actual action to be taken based on state change
# 3. Context:Accepts the client's request, it also maintains a reference to the object's current state, based on the type of request,
# concrete behavior gets called

from abc import ABCMeta, abstractmethod


class State(metaclass=ABCMeta):
    """State class"""

    @abstractmethod
    def doThis(self):
        pass


class StartState(State):
    """Concrete state classes"""

    def doThis(self):
        print("TV Switching ON ..")


class StopState(State):
    """Concrete state class"""

    def doThis(self):
        print("TV Switching Off ..")

class TVContext(State):
    """Context Class"""

    def __init__(self):
        self.state=None

    def getState(self):
        return self.state

    def setState(self,state):
        self.state=state

    def doThis(self):
        self.state.doThis()


if __name__ == "__main__":
    context=TVContext()
    context.getState()

    start=StartState()
    stop=StopState()

    context.setState(start)
    context.doThis()

    context.setState(stop)
    context.doThis()


"""
Advantages:
1. easy to add behavior
2. Improves cohesion :related functionalities in a module

Disadvantages:
1. Class Explosion: For each state one class, can increase code and thus maintenance
2. With new behavior addition, Context class needs to be updated to deal with each behavior

"""