def prime(n):
    yin = 0
    for i in range(1,n):
        if n % i == 0:
            yin +=1

        if yin > 1 or n == 1 or n == 0:
            return False
    
    return True
    
s = eval(input())
result = []

for i in range(len(s)):
    if prime(s[i]) == True:
        result.append(s[i])

print(result)

