s = input().split(' ')
lst = []
for i in range(1,len(s)):
    lst.append(f'{int(s[i]):.2f}')
lsst = list(map(float,lst))
lst.sort(reverse = True, key = lambda x: float(x))
ave = sum(lsst)/len(lsst)
print(f"{s[0]} {' '.join(map(str, lst))} {ave:.2f}")