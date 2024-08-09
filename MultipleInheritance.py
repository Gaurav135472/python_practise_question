# Base class 1
class Animal:
    def __init__(self, name):
        self.name = name

# Base class 2
class Pet:
    def __init__(self, owner):
        self.owner = owner

# Derived class
class Dog(Animal, Pet):
    def __init__(self, name, owner, breed):
        Animal.__init__(self, name)
        Pet.__init__(self, owner)
        self.breed = breed

    def details(self):
        print(f"{self.name} is a {self.breed} owned by {self.owner}")

dog = Dog("Buddy", "Alice", "Golden Retriever")
dog.details()  # Output: Buddy is a Golden Retriever owned by Alice
