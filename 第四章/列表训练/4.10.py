s = eval(input())
ave = sum(s) / len(s)
if ave.is_integer():
    print(int(ave))
else:
    print(f" {ave:.2f}")