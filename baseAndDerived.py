'''
Write a python program that creates a class Base and Derived. Use inbuilt
function issubclass and isinstance which gives boolean results.(True or
False)
'''
class BaseClass:
    def __init__(self):
        pass

class DerivedClass(BaseClass):
    def __init__(self):
        BaseClass.__init__(self)
        pass

derived=DerivedClass()
base=BaseClass()
print("Derived class is a subclass of Base class:{}".format(issubclass(DerivedClass,BaseClass)))
print("Base class is a subclass of Derived class:{}".format(issubclass(BaseClass,DerivedClass)))
print("Base class is an instance of Derived class:{}".format(isinstance(base,DerivedClass)))
print("Derived class is an instance of Base class:{}".format(isinstance(derived,BaseClass)))