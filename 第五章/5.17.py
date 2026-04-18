n = True
sum = 0
num = 0
while n == True:
    s = input()
    if s != '#':
        sum += int(s)
        num += 1

    else:
        print(num, sum)
        break
    

