h = float(input())
n = int(input())
sum = h
h /= 2
for i in range(2,n+1):
    sum += 2*h
    h /= 2  
print(f'{sum:.2f}')
