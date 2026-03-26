s = eval(input())
ave = sum(s)/len(s)
averound = round(ave)
try:
    if ave == averound:
        print(int(ave))
    else:
        print(f"{ave:.2f}")

except:
    print('error')

'''
if ave % 1 == 0:
    print(int(ave))
else:
    print(f"{ave:.2f}")

'''