class Employee:
    def __init__(self) -> None:
        # self.name = "Gaurav"
        # self.__name = "Gaurav"
        self._name = "Gaurav"

a = Employee()
# print(a.__name) not accessable because of private variable be can be access inderictly through the bellow technique
# print(a._Employee__name) 
print(a._name) 

# print(a.__dir__()) all the method which can be accessed it shows that all things