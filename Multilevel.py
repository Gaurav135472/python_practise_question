# Base class
class Animal:
    def __init__(self, name):
        self.name = name

# Intermediate class
class Mammal(Animal):
    def __init__(self, name, habitat):
        super().__init__(name)
        self.habitat = habitat

# Derived class
class Dog(Mammal):
    def __init__(self, name, habitat, breed):
        super().__init__(name, habitat)
        self.breed = breed

    def details(self):
        print(f"{self.name} is a {self.breed} that lives in {self.habitat}")

dog = Dog("Buddy", "House", "Golden Retriever")
dog.details()  # Output: Buddy is a Golden Retriever that lives in House
