class MyClass:
    def __init__(self,value) -> None:
        self._value = value
    def show(self):
        print(f"Value is {self._value}")
        
    @property
    def Ten_value(self):
        return 10*self._value
    
    @Ten_value.setter
    def Ten_value(self,new_value):
        self._value = new_value/10
    

obj = MyClass(10)
print(obj.Ten_value)
obj.show()
obj.Ten_value = 67
print(obj.Ten_value)
obj.show()


