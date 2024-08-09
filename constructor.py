
class Person: 
    def __init__(self, n, o) -> None:
        print("Hy I am a person")
        self.name = n
        self.occ = o
    def info(self):
        print(f"{self.name} is a {self.occ}")
        
a = Person("Gaurav", "Developer")
b = Person("Harry", "Tutor")
a.info()