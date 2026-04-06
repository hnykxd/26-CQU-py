s = eval(input())
dic = {}
for i in s:
    dic[i] = dic.get(i, 0) + 1

result = [ch for ch in s if dic[ch] == 1]

if len(result) == 0:
    print("False")
else:
    result.sort()
    result = [str(x) for x in result]
    print(','.join(result))