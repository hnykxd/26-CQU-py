def Fibonacci(num, n):
    for i in range (2,n):
        numnew = num[i-1] +num[i-2]
        num.append(numnew)

    return num[n-1]

num = [1,1]
n = 3
print(Fibonacci(num, n))