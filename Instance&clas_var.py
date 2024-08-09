class Employee:
    companyName = "Apple"
    owner = "Gaurav Patel"
    
    def __init__(self,name) -> None:
        self.name = name
        self.raise_amount = 0.02
    def showDetails(self):
        print(f"The name of the Employee is  {self.name} and the raise amount is {self.raise_amount} in {self.companyName} adn the owner is {self.owner}")
    
emp1 = Employee("Gaurav")
emp1.raise_amount = 0.03
emp1.companyName = "Apple India"
emp1.owner = "Gaurav"
emp1.showDetails()
emp2 = Employee("Mihir")
emp2.showDetails()
