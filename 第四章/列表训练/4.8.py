lst = eval(input())
n,m = eval(input())
if m > len(lst) or n > len(lst):
    print("error")
else:
    del lst[n:m]
    print(lst)