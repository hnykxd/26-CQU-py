s = input().split()
dic = {}
lst = []
for i in s:
    dic[i] = dic.get(i, 0) + 1

if not dic:
    print([])
else:
    maxcount = max(dic.values())
    for i in s:
        if dic[i] == maxcount and i not in lst:
            lst.append(i)
    lst.sort()
    
    for w in lst:
        print(w, maxcount)