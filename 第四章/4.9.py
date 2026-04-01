s = input().upper()

try:
    if s.startswith('$'):
        result = float(s[1:]) * 6.78
        print(f"&{result:.2f}")
    
    elif s.startswith('USD'):
        result = float(s[3:]) * 6.78
        print(f"RMB{result:.2f}")

    elif s.startswith('&'):
        result = float(s[1:]) / 6.78
        print(f"${result:.2f}")

    elif s.startswith('RMB'):
        result = float(s[3:]) / 6.78
        print(f"USD{result:.2f}")
    
    else:
        print("Error")

except ValueError:
    print("Error")
