pswd = input()
mingwen = ''

for ch in pswd:
    if 'A' <= ch <= 'Z':
        offset = ord(ch) - ord('A')
        mingwen += chr(ord('Z') - offset)
    elif 'a' <= ch <= 'z':
        offset = ord(ch) - ord('a')
        mingwen += chr(ord('z') - offset)
    else:
        mingwen += ch

print(pswd)
print(mingwen)
