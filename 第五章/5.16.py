s = int(input())
lst = []

def Fibonacci2(n): 
    a = 1
    b = 1
    for _ in range (n):
        a, b = b, a+b
    return a

for i in range(s):
    lst.append(Fibonacci2(i+2)/Fibonacci2(i+1))

result = sum(lst)
print(f'{result:.4f}')