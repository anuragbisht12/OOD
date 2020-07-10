# This create a family of products rather than just one product
# they use composition to delegate the responsibility of object creation
# unlike factory method where we use inheritance and subclasse to decide which object to create

from abc import ABCMeta, abstractmethod


class PizzaFactory(metaclass=ABCMeta):
    """Abstract Factory Class"""
    @abstractmethod
    def createVegPizza(self):
        pass

    @abstractmethod
    def createNonVegPizza(self):
        pass


class IndianPizzaFactory(PizzaFactory):
    """Concrete Factory Class"""

    def createVegPizza(self):
        return DeluxVeggiePizza()

    def createNonVegPizza(self):
        return ChickenPizza()


class USPizzaFactory(PizzaFactory):
    """Concrete Factory Class"""

    def createVegPizza(self):
        return MexicanVegPizza()

    def createNonVegPizza(self):
        return HamPizza()


# Abstract products that factories can create
class VegPizza(metaclass=ABCMeta):
    """Abstract Product Class"""

    @abstractmethod
    def prepare(self):
        pass


class NonVegPizza(metaclass=ABCMeta):
    """Abstract Product Class"""

    @abstractmethod
    def serve(self, VegPizza):
        pass


# Define concrete product classes
class DeluxVeggiePizza(VegPizza):
    """Concrete product class"""

    def prepare(self):
        print("Prepare : ", type(self).__name__)


class ChickenPizza(NonVegPizza):
    """Concrete product class"""

    def serve(self, VegPizza):
        print(type(self).__name__, " is served with chicken on ",
              type(VegPizza).__name__)


class MexicanVegPizza(VegPizza):
    """Concrete product class"""

    def prepare(self):
        print("Prepare : ", type(self).__name__)


class HamPizza(NonVegPizza):
    """Concrete product class"""

    def serve(self, VegPizza):
        print(type(self).__name__, " is served with ham on ",
              type(VegPizza).__name__)

# Pizza store
class PizzaStore:
    def __init__(self):
        pass

    def makePizzas(self):
        for factory in [IndianPizzaFactory(),USPizzaFactory()]:
            print(factory)
            self.factory=factory
            self.NonVegPizza=self.factory.createNonVegPizza()
            self.VegPizza=self.factory.createVegPizza()
            self.VegPizza.prepare()
            self.NonVegPizza.serve(self.VegPizza)


# client code
if __name__ == "__main__":
    pizza=PizzaStore()
    pizza.makePizzas()