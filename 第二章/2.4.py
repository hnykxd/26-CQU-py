import math

x1,y1 = map(float, input().replace(","," ").split())

x2,y2 = map(float, input().replace(","," ").split())

dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# 输出
print(f"{dist:.2f}")