def sushu(n):
    if n<2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2,n):
            if n % i == 0:
                return False
        return True
    
s = int(input())
for i in range(1,s+1):
    if sushu(i):
        if sushu(s - i):
            print(s,'=',i,'+',s-i)
            break

