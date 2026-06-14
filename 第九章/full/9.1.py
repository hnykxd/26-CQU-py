class shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Rectangle(shape):
    def __init__(self,w,h):
        super().__init__
        self.w = w
        self.h = h
        
    def getArea(self):
        return self.w * self.h
        
class Square(Rectangle):
    def __init__(self,side):
        super().__init__
        self.side = side
        
    def getArea(self):
        return self.side **2
        
class Circle(shape):
    def __init__(self,r):
        super().__init__
        self.r = r
        
    def getArea(self):
        return 3.14 * self.r * self.r
    
w,h = map(int,input().split())
r = int(input())
side = int(input())
print(Rectangle(w,h).getArea())
print(f"{Circle(r).getArea():.2f}")
print(Square(side).getArea())