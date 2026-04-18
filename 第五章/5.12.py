s = input()
n = int(s)
num = 0
for i in range (100,n+1):
    if i < 1000 and (i // 100)**3 + ((i // 10)%10)**3 + (i%10)**3 == i:
        print(i)
        num +=1

if num == 0:
    print('none')
