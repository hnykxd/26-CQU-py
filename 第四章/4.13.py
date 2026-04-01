def find_first_unique_char():
    try:
        
        s = input()
    except EOFError:
        s = ""

    # 处理输入为空的情况
    if not s:
        print("None")
        return

    count_dict = {}
    for char in s:
        count_dict[char] = count_dict.get(char, 0) + 1

    for char in s:
        if count_dict[char] == 1:
            print(char)
            return

    # 如果所有字符都重复了，虽然题目没说明，通常也输出 None 或特定提示
    print("None")

find_first_unique_char()
