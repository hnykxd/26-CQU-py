import math
r = eval(input("请输入圆的半径:"))
fArea = math.pi*r*r
fPerimeter = 2*r*math.pi
print(f"周长:{fPerimeter:.2f},面积:{fArea:.3f}")