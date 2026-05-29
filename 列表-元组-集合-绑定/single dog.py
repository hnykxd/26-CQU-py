n = int(input())

dic = {}
for i in range(n):
    s1,s2 = input().split(' ')
    s1 = int(s1)
    s2 = int(s2)
    dic[s1] = s2
    dic[s2] = s1
m = int(input())
people = set(map(int, input().split(' ')))
result = []
for i in people:
    if i in dic:
        if dic[i] not in people:
            result.append(i)
            
    else:
        result.append(i)       
result.sort()
print(len(result))
print(' '.join(map(str, result)))