dic = {}
while True:
    s = input().split()
    if s == ['ok']:
        break
    else:
        dic[s[0]] = dic.get(s[0], 0) + int(s[1])

print(sorted(dic.keys()))
print(sorted(dic.values()))
if 'India' in dic:
    print('yes')
else:
    print('no')
print(sum(dic.values()))

