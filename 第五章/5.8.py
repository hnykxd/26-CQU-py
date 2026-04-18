s1 = input().split(',')
s2 = eval(input())
result = []

for i in range(len(s2)):
    result.append([s1[i],s2[i]])    

print(result)