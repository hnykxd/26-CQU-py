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
    
def huiwenshu(n):
    s = str(n)
    if n != int(n) or n <0:
        return False
    elif sushu(n):
        for i in range(len(s)//2):
            if s[i] != s[len(s)-i-1]:
                return False
        return True


    
s = input()
n = float(s)
result = []
if n > 0 and n.is_integer():
    for i in range(int(n)):
        if huiwenshu(i):
            result.append(i)
    
else:
    print('illegal input')

         
print(' '.join(str(x) for x in result))