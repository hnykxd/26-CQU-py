s = input()
max_digit = ""
current = ""

for ch in s:
    if ch.isdigit():
        current += ch
    else:
        if len(current) >= len(max_digit):
            max_digit = current
        current = ""

# 处理末尾情况
if len(current) >= len(max_digit):
    max_digit = current

print(max_digit if max_digit else "No digits")

        

