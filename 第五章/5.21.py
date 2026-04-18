s = input()
max_str = ''
max_len = 0
current_len = 0
current_str = ''

for i in range(len(s)):
    if s[i].isdigit():
        current_len += 1
        current_str += s[i]
        if current_len >= max_len:
            max_str = current_str
            max_len = current_len
    else:
            current_len = 0
            current_str = ''
    
if max_len == 0:
    print('No digits')
else:
    print(max_str)    