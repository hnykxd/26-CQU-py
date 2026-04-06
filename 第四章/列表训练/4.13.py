s = list(map(int, input().split(',')))
n,m = map(int, input().split(','))
if n < -len(s) or n >= len(s):
    print("error")
else:
    target = s[n]
    for i in range(m):
        s.append(target)
    print(s)
