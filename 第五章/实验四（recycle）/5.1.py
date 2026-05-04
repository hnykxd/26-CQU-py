s1 = input().split(',')
s2 = list(map(int, input().split(',')))

result = [[s1[i], s2[i]] for i in range(len(s1))]
result.sort(key=lambda x: x[1])
print(result)
