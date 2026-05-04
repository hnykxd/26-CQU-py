
s = int(input())


lst = []

while True:
    if s % 2 != 0 and s != 1:
        s = s * 3 + 1
        lst.append(s)
    elif s % 2 == 0:
        s //= 2
        lst.append(s)
    else:
        
        break

print(','.join(str(x) for x in lst))
    