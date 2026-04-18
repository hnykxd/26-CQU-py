num = eval(input())
result = []
dic = {}
for x in num:
    dic[x] = dic.get(x,0)+1
for i in num:
    if dic[i] == 1:
        result.append(i)
result.sort()
if min(dic.values()) > 1:
    print('False')
else:
    print(",".join(map(str, result)))

