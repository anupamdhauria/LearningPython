"""
The __init__() function is called automatically every time the class is being used to create a new object.
"""
class car:
    def __init__(self,modelname,year):
        self.modelname=modelname
        self.year=year
    def display(self):
        print(self.modelname,self.year)

    def __str__(self):
        return f"{self.modelname} {self.year}"

c1=car('Toyota',2016)
print(c1)

#modift car year
c1.year=2001
print(c1)
print("calling display method")
c1.display()

#delete object properties
del c1.year
c1.display()

#del entire object
del c1
print(c1)








