# Behavioral Pattern
# All the information regarding the choices are encapsulated in an object that can be used later to take an action
# Command: this declares an interface to execute an operation
# ConcreteCommand: This defines binding between receiver object and sets its receiver
# Client: This creates concretecommand object and set its receiver
# Invoker: this asks concretecommand to carry out the request
# receiver: this knows how to perform the operations asssociated with carrying out the request

# Flow: Client asks for a command to be executed. The invoker takes the command, encapsulates it, and places it in a queue.
# The ConcreteCommand class is in charge of the requested command and asks the receiver to perform the given action.

# Stock broker agent in buying and selling of the stocks, you can still make requests to 
# stock exchange on sunday to get the work done on monday.

from abc import ABCMeta, abstractmethod

class Order(metaclass=ABCMeta):
    """Command object is created using this interface"""

    @abstractmethod
    def execute(self):
        pass

class BuyStockOrder(Order):
    """ ConcreteCommand class """
    def __init__(self,stock):
        self.stock=stock

    def execute(self):
        self.stock.buy()

class SellStockOrder(Order):
    """ConcreteCommand class"""

    def __init__(self,stock):
        self.stock=stock

    def execute(self):
        self.stock.sell()


class StockTrade:
    """Receiver object class"""

    def buy(self):
        print("You will buy stocks")

    def sell(self):
        print("You will sell stocks")
        
class Agent:
    """Invoker class"""

    def __init__(self):
        self._orderQueue=[]

    def placeOrder(self,order):
        self._orderQueue.append(order)
        order.execute()


if __name__ == "__main__":
    
    # client
    stock=StockTrade()
    buyStock=BuyStockOrder(stock)
    sellStock=SellStockOrder(stock)

    # Invoker
    agent=Agent()
    agent.placeOrder(buyStock)
    agent.placeOrder(sellStock)


# Application in software applications
# Redo or rollback operations

# Asynchronous task execution
# invoker object maintains a queue of requests and send these tasks to the receiver objects

# Advantage:
# decouples
# sequencing
# rollback

# disadvantages
# high number of classes and objects working together to achieve a goal, need to be implemented carefully

# we can define the design without receiver and concretecommand too

# We can either use queue for sequencing or stack for rollback mechanisms