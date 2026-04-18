s = input().split(',') 
result = []
for i in range(int(s[1])):
    result.append(int(s[0])+int(s[2])*i)
print(result)   