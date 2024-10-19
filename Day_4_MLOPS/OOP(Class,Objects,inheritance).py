#Defining and creating an object
class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Model: {self.model}, Year: {self.year}")

# Creating an object
my_car = Car("Tesla Model S", 2022)
my_car.display_info()

#Inheritance in python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks.")

# Using inheritance
dog = Dog("Buddy")
dog.speak()  # Buddy barks

#polymorphism in methods
class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows.")

def animal_sound(animal):
    animal.speak()

# Both Dog and Cat classes use the same method name 'speak' but behave differently
animal_sound(Dog("Charlie"))
animal_sound(Cat("Whiskers"))
