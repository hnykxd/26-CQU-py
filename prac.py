s = input()
letter = 0
space = 0
digit = 0
other = 0

for i in range(0, len(s)):
    if s[i].isalpha():
        letter+=1
    elif s[i].isspace():
        space+=1
    elif s[i].isdigit():
        digit+=1
    else:
        other+=1

print(letter, space, digit, other)