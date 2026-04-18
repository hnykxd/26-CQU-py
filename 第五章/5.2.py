s = eval(input())
s1 = sorted(s, reverse=True)
result = ''.join(map(str, s1))
if int(result) == 0:   
    print('0')
else:
    print(result)