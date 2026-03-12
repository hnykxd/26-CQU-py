import math
l1 = float(input())
l2 = float(input())
V = 4/3*math.pi*(0.5*l1)*(0.5*l1)*(0.5*l1) + 4/3*math.pi*(0.5*l2)*(0.5*l2)*(0.5*l2)
a = V**(1/3)
print(f"正方体边长为:{a:.2f}.")

