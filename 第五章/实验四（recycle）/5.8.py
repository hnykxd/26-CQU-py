import math
k = int(input())
e = 1
for i in range(1,k+1):
    e += 1/math.factorial(i)
print(f'{e:.10f}')