"""
Chain of responsibility
"""

"""
Call Center: Imagine you have a call center with three levels of employees: respondent, manager,
and director. An incoming telephone call must be first allocated to a respondent who is free. If the
respondent can't handle the call, he or she must escalate the call to a manager. If the manager is not
free or not able to handle it, then the call should be escalated to a director. Design the classes and
data structures for this problem. Implement a method d i s p a t c h C a l l ( ) which assigns a call to
the first available employee.

"""


from abc import ABCMeta, abstractmethod
from random import random


class CallCenter(metaclass=ABCMeta):
    """
    A call center class that will be inherited from by the director

    Attributes:
        name: Name of the employee
        number: Mobile phone number of the employee
        level: Define level of the employee - respondent, manager or director
    """

    def __init__(self, name, number, level):
        self.name = name
        self.number = number
        self.level = level

    def canEmployeeHandle(self):
        canHandle = random()
        if canHandle > 0.5:
            return True
        else:
            return False

    def isEmployeeBusy(self):
        busy = True if random() <= 0.5 else False
        return busy

    @classmethod
    def dispatchCall(self,cls):
        return cls.answerCall()

    @abstractmethod
    def answerCall(self):
        """Print a string indicating that this employee is currently
        answering the call or propogate up the chain"""
        pass


class Director(CallCenter):
    """
    A class definition for the director who will be the third in chain
    to answer the call
    """

    def answerCall(self):
        print("The director is now on call with you")


class Manager(Director):
    """
    A class definition for the manager who will be the second in chain to
    answer the call
    """

    def answerCall(self):
        if not self.isEmployeeBusy() and self.canEmployeeHandle():
            print("The manager is answering your call")
        else:
            print("Manager is busy, escalating the call to the Director")
            super(Manager, self).answerCall()


class Respondent(Manager):
    canHandle = random()  # class variable to check if respondent can handle call
    """
    A class definition for the respondent who will be the first in chain
    to answer the call
    """

    def answerCall(self):
        if not self.isEmployeeBusy() and self.canEmployeeHandle():
            print("The respondent is answering your call")
        else:
            print("Employee is busy, escalating the call to the Manager")
            super(Respondent, self).answerCall()


if __name__ == "__main__":
    director = Director("Alex", "+17654736791", "director")
    manager = Manager("Unai", "+331577285782", "manager")
    respondent = Respondent("Mark", "+16574872817", "respondent")

    CallCenter.dispatchCall(respondent)
