x = int(input())

day2 = 2/(1 - x/100)

day1 = (day2 + 1)/(1 - x/100)

day0 = (day1 + 1)/(1-x/100)
print(f"猴子第1天摘得{day0:.0f}个桃.")
