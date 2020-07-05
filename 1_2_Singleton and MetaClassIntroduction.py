# class is instance of its metaclass
# gives opportunity to create classes of own type using predefined python classes
class MyInt(type):
    def __call__(cls,*args,**kwds):
        print("***HEre's my Int****",args)
        print("Now do whatever you want with these objects")
        return type.__call__(cls,*args, **kwds)

class int(metaclass=MyInt):
    """
    MyInt class __call__ method will be called which means metclass now controls instantiation of object
    definition of a class is decided by its metaclass, so when we create a class object 3 entities are involved
    name : name of the class
    base: base class
    dict: this is attribute variable
    """
    def __init__(self,x,y):
        self.x=x
        self.y=y

i= int(4,5)
# Output
# ***HEre's my Int**** (4, 5)
# Now do whatever you want with these objects

# Singleton and metclasses together can be used to control the class and object instantiation
# meta class overrides __new__ and __init__ method

class MetaSingleton(type):
    _instances={}
    def __call__(cls,*args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls]=super(MetaSingleton,cls).__call__(*args, **kwargs)
        
        return cls._instances[cls]

class Logger(metaclass=MetaSingleton):
    pass


log1=Logger()
log2=Logger()
print(log1,log2)



# *******************************************Actual Application ***********************************************






