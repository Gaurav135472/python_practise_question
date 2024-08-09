class Person:
    name = "Gaurav"
    occupation = "Software Development"
    networth = 10
    def info(self):
        print(f"{self.name} is a  {self.occupation}")

a = Person()
a.name = "Gaurav"
a.occupation = "Accountant"
print(a.occupation, a.name)
a.info()