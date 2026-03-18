inf = input()

try:
    if inf in ["3","4","5"]:
        print("spring")
    
    elif inf in ["6","7","8"]:

        print("summer")

    elif inf in ["9","10","11"]:

        print("autumn")

    elif inf in ["12","1","2"]:
        print("winter")

    else:
        print("error")

except ValueError:
    print("error")