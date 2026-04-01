s = input()
k = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
yushu = [0,1,2,3,4,5,6,7,8,9,10]
jiaoyan = ['1','0','X','9','8','7','6','5','4','3','2']
sum = 0
sum1 =0
try:
    for i in range(17):
        sum1 = int(s[i])*int(k[i])
        sum += sum1

    mod = sum % 11
    for i in range(11):
        if mod == yushu[i]:
            if jiaoyan[i] == s[17]:
                print("Correct")
            else:
                print("Wrong")

    if len(s) != 18:
        print("Error")

except (ValueError, IndexError):
    print("Error")


