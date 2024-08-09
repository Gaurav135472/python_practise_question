# Base class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")

# Derived class 1 - Single Inheritance
class Mammal(Animal):
    def __init__(self, name, habitat):
        super().__init__(name)
        self.habitat = habitat

# Derived class 2 - Single Inheritance
class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan
    
    def fly(self):
        print(f"{self.name} can fly with a wingspan of {self.wingspan} meters")

# Derived class 3 - Multiple Inheritance
class Bat(Mammal, Bird):
    def __init__(self, name, habitat, wingspan):
        Mammal.__init__(self, name, habitat)
        Bird.__init__(self, name, wingspan)
    
    def details(self):
        print(f"{self.name} is a bat that lives in {self.habitat} and has a wingspan of {self.wingspan} meters")

# Derived class 4 - Hierarchical Inheritance
class Dog(Mammal):
    def __init__(self, name, habitat, breed):
        super().__init__(name, habitat)
        self.breed = breed
    
    def speak(self):
        print(f"{self.name} barks")

# Derived class 5 - Hierarchical Inheritance
class Cat(Mammal):
    def __init__(self, name, habitat, color):
        super().__init__(name, habitat)
        self.color = color
    
    def speak(self):
        print(f"{self.name} meows")

# Creating instances of the classes
bat = Bat("Bruce", "Cave", 1.5)
dog = Dog("Buddy", "House", "Golden Retriever")
cat = Cat("Whiskers", "House", "Black")

# Displaying details and behaviors
bat.details()  # Output: Bruce is a bat that lives in Cave and has a wingspan of 1.5 meters
bat.speak()    # Output: Bruce makes a sound
bat.fly()      # Output: Bruce can fly with a wingspan of 1.5 meters

dog.speak()    # Output: Buddy barks
cat.speak()    # Output: Whiskers meows
