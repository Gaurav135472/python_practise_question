
class Employee:
    def __init__(self,name,id) -> None:
        self.name = name
        self.id = id

class Programmer(Employee):
    def __init__(self, name, id,lang) -> None:
        super().__init__(name, id)
        self.lang = lang
        
rohan = Employee("Gaurav Patel", "420")
harry = Programmer("Harry", "4202", "HIndi")
print(harry.name)
print(harry.id)
print(harry.lang)