num = list(map(int, input().split()))

maxnum = max(num)
minnum = min(num)


std = [(value - minnum) / (maxnum - minnum) for value in num]
tem = [f"{i:.6f}" for i in std]
strnum = "-".join(tem)
print(strnum)
