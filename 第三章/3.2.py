def get_color(number):
    
    if number < 0 or number > 36:
        return "error"

    
    
    if number == 0:
        return "green"
    
    if 1<= number <= 10 or 19 <= number <= 28:
        if number % 2 == 0:
            return "black"
        else:
            return "red"
    
    if 11 <= number <= 18 or 29 <= number <= 36:
        if number % 2 == 0:
            return "red"
        else:
            return "black"
try:
    user_input = int(input())
    result = get_color(user_input)
    print(result)
except ValueError:
    print("error")