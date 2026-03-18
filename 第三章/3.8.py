math = float(input())
chinese = float(input())

try:
    if math >= 99 and chinese >= 99:
        print("You won a scholarship of 500 yuan!")

    elif math < 30 and chinese < 30:
        print("You need to relearn!")

except ValueError:
    print("error")