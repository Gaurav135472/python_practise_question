from turtle import circle, shape


class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def area(self):
        return self.x * self.y
    
class Circle(Shape):
    def __init__(self,redius):
        self.redius = redius
        super().__init__(redius,redius)
    
    def area(self):
        return 3.14 * super().area()
    
rec = Circle(3.14)
print(rec.area()
)