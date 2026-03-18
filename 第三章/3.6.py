inf = input().upper()

try:
    if inf.startswith('$'):
        result = float(inf[1:]) * 6.78
        print(f"￥{result:.2f}")
    
    elif inf.startswith('USD'):
        result = float(inf[3:]) * 6.78
        print(f"RMB{result:.2f}")

    elif inf.startswith('￥'):
        result = float(inf[1:]) / 6.78
        print(f"${result:.2f}")

    elif inf.startswith('RMB'):
        result = float(inf[3:]) / 6.78
        print(f"USD{result:.2f}")
    
    else:
        print("Error")

except ValueError:
    print("Error")