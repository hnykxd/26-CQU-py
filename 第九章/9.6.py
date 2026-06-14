class BMI:
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    
    def getBMI(self):
        return self.weight / self.height ** 2
    
    def getStatus(self):
        bmi = self.getBMI()
        if bmi < 18.5:
            return "underweight"
        elif bmi < 25:
            return "ideal"
        elif bmi < 30:
            return "overweight"
        else:
            return "obesity"    