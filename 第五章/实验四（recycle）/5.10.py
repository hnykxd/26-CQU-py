def findgongyue(a, b):
    maxnum = 0
    for i in range(1,a+1):
        if a%i ==0 and b %i == 0:
            maxnum = i
    return maxnum
a,b = map(int,input().split())
c = findgongyue(a,b)
print(a//c,b//c)