s1 = eval(input())
s = ''.join(s1)
dic = {}
for ch in s:
    dic[ch] = dic.get(ch, 0) + 1

for key in sorted(dic):
    print(key, dic[key], sep = ',')
