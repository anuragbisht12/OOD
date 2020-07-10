# The GoF have identified in their work 23 design patterns that can be grouped into three categories:
# Creational Patterns: These are all about hiding the creation logic and avoid using constructors directly. 
# These patterns make the programs more flexible by allowing us to decide what patterns get created for 
# each given use case(e.g. Singleton pattern).
# Structural Patterns: These patterns use composition and inheritance to obtain new functionality(e.g. Adapter pattern).
# Behavioral Patterns: They are specifically concerned with the interaction and communication between objects
#  while remaining loosely coupled(e.g. Observer pattern).

# Singleton
# The Singleton Design Pattern is one of the simplest and most famous Creational design patterns.
#  It provides us with a way to only have a SINGLE instance of a given object and a global point of access to it.


# By providing us with a single global object, the Singleton pattern allows us to control concurrent access to shared resources.
# Eg: logging

class Singleton:
    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super().__new__(self)
        return self.instance

# or
class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton).__new__(cls)
        return cls.instance

# Lazy instantiation of Singleton class


class Singleton2:
  _instance = None

  def __init__(self):
    if not Singleton2._instance:
      print("__init__ method called but nothing is created")
    else:
      print("instance already created:", self.getInstance())

  @classmethod
  def getInstance(cls):
    if cls._instance is None:
      cls._instance = Singleton2()
    return cls._instance


if __name__ == "__main__":
    print("Object: ", Singleton())
    print("Object: ", Singleton())


    # Lazy instantiation
    # class initialized, but object not created
    s = Singleton2()
    s1 = Singleton2()

    # This returns None although the object is initialized
    print(s._Singleton2_instance)
    print(s1._Singleton2_instance)

    # We now explicitly initialize the object:
    s.getInstance()
    s1.getInstance()

    # Which is now accessible
    print(s._Singleton2__instance)
    print(s1._Singleton2__instance)




# Monostate Singleton

# 1st way
class Borg:
  """
  Concept of all objects sharing the same state is monostate pattern
  """
  __shared_state={"1":"2"}
  def __init__(self):
    self.x=1
    self.__dict__=self.__shared_state
    pass

b=Borg()
b1=Borg()
b.x=4


# 2.Another way
class Borg(object):
  """Monostate using new method"""
  _shared_state={}
  def __new__(cls,*args, **kwargs):
    obj =super(Borg,cls).__new__(cls, *args, **kwargs)
    obj.__dict__=cls._shared_state
    return obj
    

