def get_color(number):
    
    if number < 0 or number > 36:
        return "error"

    
    
    if number == 0:
        return "green"
    
    # 1-10号：奇红偶黑
    if number == 1: return "red"
    if number == 2: return "black"
    if number == 3: return "red"
    if number == 4: return "black"
    if number == 5: return "red"
    if number == 6: return "black"
    if number == 7: return "red"
    if number == 8: return "black"
    if number == 9: return "red"
    if number == 10: return "black"
    
    # 11-18号：奇黑偶红
    if number == 11: return "black"
    if number == 12: return "red"
    if number == 13: return "black"
    if number == 14: return "red"
    if number == 15: return "black"
    if number == 16: return "red"
    if number == 17: return "black"
    if number == 18: return "red"
    
    # 19-28号：奇红偶黑
    if number == 19: return "red"
    if number == 20: return "black"
    if number == 21: return "red"
    if number == 22: return "black"
    if number == 23: return "red"
    if number == 24: return "black"
    if number == 25: return "red"
    if number == 26: return "black"
    if number == 27: return "red"
    if number == 28: return "black"
    
    # 29-31号（及后续到36）：奇黑偶红
    if number == 29: return "black"
    if number == 30: return "red"
    if number == 31: return "black"
    if number == 32: return "red"
    if number == 33: return "black"
    if number == 34: return "red"
    if number == 35: return "black"
    if number == 36: return "red"

# --- 测试部分 ---
try:
    user_input = int(input())
    result = get_color(user_input)
    print(result)
except ValueError:
    print("error")