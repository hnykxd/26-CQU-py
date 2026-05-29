n = eval(input())
s= set()

for i in range(len(n)-1,-1,-1):
    if n[i] not in s:
        s.add(n[i])
    else:
        n.pop(i)    
print(n)
    