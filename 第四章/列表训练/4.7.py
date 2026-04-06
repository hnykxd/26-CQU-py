n, m, l = map(int,input().split(','))
result = []
for i in range(m):
    result.append(n+i*l)

print(result)