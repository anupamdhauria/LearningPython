"""
The self parameter is a reference to the current instance of the class,
and is used to access variables that belong to the class.
It does not have to be named self , you can call it whatever you like,
but it has to be the first parameter of any function in the class:
"""
class Person:
    def __init__(anupam,age,adhar):
        anupam.age=age
        anupam.adhar=adhar

    def print(anupam):
        n1='\n' #new line in fstring
        print(f"name: anupam{n1}age:{anupam.age}{n1}Adhar Number: {anupam.adhar}")



#creating a object
person1=Person(26,78654567875456)
person1.print();