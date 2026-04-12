def Fibonacci(num, n): #求前n个数
    for i in range (2,n):
        numnew = num[i-1] +num[i-2]
        num.append(numnew)

    return num[n-1]

def Fibonacci2(n): #仅仅求最后一个数
    a = 1
    b = 1
    for _ in range (n):
        a, b = b, a+b
    return a

num = [1,1]
n = 3
print(Fibonacci(num, n))