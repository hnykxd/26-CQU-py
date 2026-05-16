s1 = eval(input())
s = ''.join(s1)
dic = {}
for ch in s:
    dic[ch] = dic.get(ch, 0) + 1

for key in sorted(dic):
    print(key, dic[key], sep = ',')
    

# s1 = eval(input())
# s = ''.join(s1)
# lst = sorted(list(s))
# for i in range(len(lst)):
#     if lst[i] != lst[i-1]:
#         print(lst[i], lst.count(lst[i]),sep = ',')