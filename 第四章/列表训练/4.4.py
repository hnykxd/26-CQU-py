n = int(input())

s = [ch for ch in range(1, n+1)]

del s[0]
s.append(1)
print(s)