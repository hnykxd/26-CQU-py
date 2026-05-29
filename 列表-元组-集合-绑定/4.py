s1 = input().split(',')
s2 = list(map(int, input().split(',')))
result = []
for i in range(len(s2)):
    result.append([s1[i],s2[i]])
result.sort(key = lambda x: x[1])
print(result)