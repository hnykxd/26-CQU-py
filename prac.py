import math
def calculate_e(n):
    e = 1
    for i in range(1,n+1):
        e += 1/math.factorial(i)
    print(f'{e:.6f}')
    return