from abc import ABC, abstractmethod

# Define the abstract class Animal
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

# Subclass Dog inheriting from Animal
class Dog(Animal):
    def sound(self):
        return "Bark"

# Subclass Cat inheriting from Animal
class Cat(Animal):
    def sound(self):
        return "Meow"
