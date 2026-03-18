import math
x = float(input())

try:
    if x < 20:
        result = 6*x**2 +1

    elif 20 <= x < 40:
        result = math.sqrt(3*x - 60)

    else:
        result = 100/(x+1)
    print(f"{result:.2f}")

except ValueError:
    print("error")