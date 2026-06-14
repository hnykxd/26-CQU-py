class Shape:
    def __init__(self,sName):
        self.sName = sName
        
class Rectangle(Shape):
    def __init__(self,sName,w,h):
        super().__init__(sName)
        self.w = w
        self.h = h
        
    def getArea(self):
        return self.w * self.h
      