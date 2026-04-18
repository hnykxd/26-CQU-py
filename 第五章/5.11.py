s1 = input().split(',')
s2 = input().split(',')
result = s1.copy()
if int(s2[0]) > len(s1) - 1:
    print('error')
else:
    for _ in range(int(s2[1])):
        result.append(s1[int(s2[0])])
    print(list(map(int, result)))
