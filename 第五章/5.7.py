s = eval(input())
try:
    for i in range(s.count(max(s))):    
        s.remove(max(s))
    for i in range(s.count(min(s))):

        s.remove(min(s))
    print(s)
except:
    print([])
