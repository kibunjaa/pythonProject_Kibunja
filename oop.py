# Object-Oriented Programming is a way of computer programming using the idea of “objects” to represents data and methods
# class
# Objects are an instance of a class. It is an entity that has state and behavior.
# Inheritance
# Polymorphism
# Encapsulation
# Abstraction
# self-used to reference class instances/ variables

class Vehicles:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color
    def SayCar(self):
        print("Your car is a", self.make, self.model, "and it is of color", self.color)

class Trucks(Vehicles):
    def __init__(self, make, model, color):
        super().__init__(make, model, color)
Vehicles1 = Trucks("DAF", "XF", "Green")
Vehicles1.SayCar()

# Vehicle1 = Vehicles("Toyota", "TX", "Black")
# print(Vehicle1.make)
# print(Vehicle1.color)
# print(Vehicle1.model)

# Vehicle1.SayCar()