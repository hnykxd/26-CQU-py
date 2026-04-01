lst = eval(input())
n, m = map(int, input().split(','))
try:
    if n > len(lst) or m > len(lst):
        print('error')
    else:
        del lst[n:m]
        print(lst)
    
except:
    print("error")
