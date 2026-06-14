with open('data.txt','r')as f:
    for line in f:
        lst = []
        line = line.split('')
        for i in line:
            if i.islower():
                lst.append(i.upper())
            if i.isupper():
                lst.append(i.lower())
        print(''.join(lst))