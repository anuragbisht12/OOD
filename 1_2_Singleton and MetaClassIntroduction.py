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
# Database read write objects application

import sqlite3
class MetaSingleton(type):
    _instances={}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls]= super(MetaSingleton,cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=MetaSingleton):
    connection=None
    def connect(self):
        if self.connection is None:
            self.connection=sqlite3.connect('db.sqlite3')
            self.cursorobj=self.connection.cursor()
        return self.cursorobj

if __name__ == "__main__":
    db1=Database().connect()
    db2=Database().connect()

    print("Database objects created DB1: ", db1)
    print("Database objects created DB1: ", db2)



# ******************Application 2: Health check Service**********************************

class HealthCheck:
    _instance =None
    def __new__(cls,*args,**kwargs):
        if not HealthCheck._instance:
            HealthCheck._instance=super(HealthCheck,cls).__new__(cls, *args, **kwargs)
        return HealthCheck._instance
    
    def __init__(self):
        self._servers=[]

    def addServer(self):
        """Add new server"""
        self._servers.append("Server 1")
        self._servers.append("Server 2")
        self._servers.append("Server 3")
        self._servers.append("Server 4")

    def changeServer(self):
        """
        Change the server
        """
        self._servers.pop()
        self._servers.append("Server 5")


if __name__ == "__main__":
    hc1=HealthCheck()
    hc2=HealthCheck()

    hc1.addServer()
    print("Schedule health check for servers (1)..")
    for i in range(4):
        print("Checking ", hc1._servers[i])

    hc2.changeServer()
    print("Schedule health check for servers (2)..")
    for i in range(4):
        print("Checking ", hc2._servers[i])


    



