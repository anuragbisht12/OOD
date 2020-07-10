# Structural pattern
# Client: which wants the action to be performed
# Proxy: agent, which provides access to the real subject
# Subject: provides representation for both, realsubject and proxy.vProxy and realsubject implements subject ,  action to be performed
# real subject: defines the real object that proxy represents
from abc import ABCMeta,abstractmethod

class Payment(metaclass=ABCMeta):
    """Subject Class acts as interface which real subject and proxy class will implement"""

    @abstractmethod
    def do_pay(self):
        pass

class Bank(Payment):
    """Real subject class"""

    def __init__(self):
        self.card=None
        self.account=None
    
    def _getAccount(self):
        self.account=self.card  # assuming card number andd account number are same
        return self.account

    def _hasFunds(self):
        print("Bank: Checking if ",self._getAccount(), " has enough funds.")
        return True

    def setCard(self,card):
        self.card=card

    def do_pay(self):
        if self._hasFunds():
            print("Bank: Paying the merchant.")
            return True
        else:
            print("Bank: Sorry not enough fun")
            return False


class DebitCard(Payment):
    """Proxy Class"""

    def __init__(self):
        self.bank=Bank()

    def do_pay(self):
        card=input("Proxy: Punch in card number: ")
        self.bank.setCard(card)
        return self.bank.do_pay()

class You:
    """Client class"""

    def __init__(self):
        print("You: lets buy the denim shirt")
        self.debitCard=DebitCard()
        self.isPurchased=None

    def make_payment(self):
        self.isPurchased=self.debitCard.do_pay()

    def __del__(self):
        if self.isPurchased:
            print("You: Wow the denim shirt is mine.")
        else:
            print("You: I should earn more :( ")

if __name__ == "__main__":
    you=You()
    you.make_payment()

# Advantages: can help improve performance of the application by caching heavy objects
# delegation only if permissions are right
# remote proxies can help interactions with remote servers

# Types:
# Virtual Proxy:create placeholder for image, load only when clicked
# remote proxy: connect to remote services and provide local representation of remote object
# Protective Proxy: controls access to the sensitive matter objects
# Smart proxy: interpose additional actions if required

# Comparing facade and proxy
# slight difference

# Decorator: adds behavior to the object that it decorates at runtime,  runtime
# while proxxy controls access to the object compile time

