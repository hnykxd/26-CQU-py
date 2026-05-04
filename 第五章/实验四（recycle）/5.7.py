s = input()
lst = []
num = 0
let = 0
for i in range(len(s)):
    if s[i].isdigit():
        num +=1
    elif s[i].isalpha():
        if s[i].islower():
            let += 1
            lst.append(s[i])
        
    elif s[i] == '#':
        break
    
print(num,',',let,sep='')
print(''.join(lst))