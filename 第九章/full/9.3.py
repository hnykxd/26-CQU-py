class Student:
    def __init__(self, sName, sAge, sscore):
        self.sName = sName
        self.sAge = sAge
        self.sscore = sscore
        
    def getName(self):
        return self.sName
    
    def getAge(self):
        return self.sAge
    
    def getScore(self):
        return max(self.sscore)
    
s = input().split(",")
name = s[0]
age = int(s[1])
score = list(map(int, s[2:]))
print (f"name: {Student(name, age, score).getName()}")
print (f"age: {Student(name, age, score).getAge()}")
print (f"max_score: {Student(name, age, score).getScore()}")