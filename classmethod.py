# class Employee:
#     company = "Apple"
#     def show(self):
#         print(f"the {self.value} and company is {self.company}")
#     @classmethod
#     def changeCompany(cls, newCompany):
#         cls.company = newCompany

# e1 = Employee()
# e1.value = "Gaurav"   
# e1.show()
# e1.changeCompany(("Gaurav"))
# e1.show()
# print(Employee.company)


class Employee:
    def __init__(self,name,company) -> None:
        self.name = name 
        self.company = company
    
    @classmethod
    def fromstr(cls,string):
        return cls(string.split("-")[0],string.split("-")[1])

e1 = Employee("Gaurav",1200)
print(e1.name)
print(e1.company)

string = "Gaurav-1200"
e2 = Employee.fromstr(string)
print(e2.name)
print(e2.company)