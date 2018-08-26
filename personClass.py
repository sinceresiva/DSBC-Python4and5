'''
Write a python program that creates base class Person which has two
methods
'''
class Person:
    def __init__(self, first, last):
        self.firstName=first
        self.lastName=last

    def __str__(self):
        return "{} {}".format(self.firstName,self.lastName)

class Employee(Person):
    def __init__(self,first,last):
        super().__init__(first,last)

emp=Employee("Siva","Subramanian")
print(emp)