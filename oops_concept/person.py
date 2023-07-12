"""
The __str__() function controls what should be returned when the class object is represented as a string.

If the __str__() function is not set, the string representation of the object is returned:

"""

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name,self.age)

    def __str__(self):
        return f"{self.name} {self.age}"

p1=Person("Anupam",28)
print(p1)
