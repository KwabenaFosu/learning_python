


#Define a class
class Dog:
    pass

''' ._init_()defines properties of all instance objects
Sets the state of the object by assigning the values of the objects properties (initializes each new instance of a class)
First paramater must always be self'''

class Dog:
   species = "cannis familiaris"     # class atrribute
   def __init__(self,age,name):
       self.age = age                # instance attribute
       self.name = name
pass

'''a = Dog()
b = Dog ()  # Created or instanciated different objects of class Dog stored in different memory addresses
a == b
pass'''




class Dog:
   species = "cannis familiaris"   
   def __init__(self,name,age):
       self.age = age               
       self.name = name

buddy = Dog("Buddy", 9)    #Creates an instance of the Dog class stored in a variable
miles = Dog("Miles", 4)


print(buddy.name)         # Access the attributes of an instance
print(buddy.species)      # Access class attributes



class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Instance method
    def __str__(self):              # Defines a string method
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"


buddy = Dog("Buddy", 9)   
miles = Dog("Miles", 4)


print(buddy)      
print(miles)





