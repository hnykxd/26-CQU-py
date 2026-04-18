s = eval(input())
dic = {}

for i in range(len(s)-1,-1,-1):
    if s[i] in dic:
        s.pop(i)
    else:
        dic[s[i]] = 1

print(s)  