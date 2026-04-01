pasw = input()

teshu = "~!@#$%^&*()_=-/,.?<>;:[]{}|\\"
def detection(a):
    strong = 0
    if len(a) >=8:
        strong+=1

    if any(i.isdigit() for i in a):
        strong+=1

    if any(i.islower() for i in a):
        strong+=1

    if any(i.isupper() for i in a):
        strong += 1

    if any(i in teshu for i in a ):
        strong +=1  

    return strong

print(detection(pasw))
