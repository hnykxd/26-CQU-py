s = eval(input())
result = []
def sushu(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True
        
for i in range(len(s)):
    if sushu(s[i]):
        result.append(s[i])
print(result)