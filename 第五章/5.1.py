s = input()
dic = {}
if not s:
    print('None')
else:
    for i in s:
        dic[i] = dic.get(i,0)+1
for x in s:
    if dic[x] == 1:
        print(x)
        break
