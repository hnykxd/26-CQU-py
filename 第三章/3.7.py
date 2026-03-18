len = float(input())
wid = float(input())

try:
    if len <= 0 or wid <= 0:
        print("illegal data")
    elif len == wid:
        print("It's a square")

    else:
        print("It's a rectangle")

except ValueError:
    print("illegal data")