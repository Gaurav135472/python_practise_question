# a = int(input("Enter any value between 5 and 9"))

# if(a<5 or a>9):
#     raise ValueError("Value should be between 5 and 9")

# print("There we go")

class adultExcenption(Exception):
    def __init__(self,message = "The given person is not adult yet") -> None:
        self.message = message
        super().__init__(self.message)

class Person():
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
        self.get_minor_age()
        self.display_person()
    
    def get_minor_age(self):
        if self.age > 18 :
            print ("he is major")
        else :
            raise adultExcenption()
        
    def display_person(self):
        print(f"The name of the person is {self.name} and the age is {self.age}")
        

    print(adultExcenption())
    
p1 = Person("Gaurav", 17)
    
# age = int(input("Enter your age"))

# if age > 18 :
#    print ("he is major")
# else :
#     raise ismajor("Only 18+ allow")

