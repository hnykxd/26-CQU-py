s1 = list(input().split(','))
s2 = eval(input())
s = []
for i in range (len(s1)):
    s.append([s1[i],s2[i]])

print(s)