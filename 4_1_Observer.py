# Behavioral pattern
# Recap
# Creational pattern: Code is independent of the type of object created
# Structural pattern: simplify the structure and identify the relationships between classes and objects
# Behavioral pattern: Focuses while the objects should be able to interact with each other,  they should be loosely coupled
# they manage the interaction between objects and manage one to many dependencies on the objects

# Observer pattern
# Subject: Main producer class
# Observer:listens to subject class
# Concrete observer: It implements observer interface to keep the state consistent with changes in the subject
from abc import ABCMeta, abstractmethod


class NewsPublisher:
    """Subject class"""

    def __init__(self):
        self._subscribers = []
        self._latestNews = None

    def attach(self, subscriber):
        self._subscribers.append(subscriber)

    def detach(self):
        return self._subscribers.pop()

    def subscribers(self):
        return [type(x).__name__ for x in self._subscribers]

    def notifySubscribers(self):
        for sub in self._subscribers:
            sub.update()

    def addNews(self, news):
        self._latestNews = news

    def getNews(self):
        return "Got news: ", self._latestNews


class Subscriber(metaclass=ABCMeta):
    """Observer class"""

    @abstractmethod
    def update(self):
        pass


class SMSSubscriber:
    """Concrete Observer classes"""

    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())


class EmailSubscriber:
    """Concrete Observer Class"""

    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())


class AnyOtherSubscriber:
    """Concrete Observer Class"""

    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())


if __name__ == "__main__":
    news_publisher=NewsPublisher()

    for Subscribers in [SMSSubscriber, EmailSubscriber, AnyOtherSubscriber]:
        Subscribers(news_publisher)
    print("Subscribers: ", news_publisher.subscribers())

    news_publisher.addNews("Hello World! ")
    news_publisher.notifySubscribers()

    print("Detached: ", type(news_publisher.detach()).__name__)
    print("Subscribers: ",news_publisher.subscribers())

    news_publisher.addNews("My second News! ")
    news_publisher.notifySubscribers()


# 2 ways of notifying the observers
# Pull:Subject broadcasts to all registered observers when there is any change
# Observer pulls the required data from the subscriber

# push: subject sends the information to the registered observerss

# advantage:
# supports principle of loose coupling

# disadvantages
# involves inheritance between observer and concrete classes
# notifications cna times be undependable and result in race condition