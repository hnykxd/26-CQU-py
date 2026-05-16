dic = {}
while True:
    n = input()
    if n == 'q':
        break
    else:
        dic[n] = dic.get(n, 0) + 1
    
max_key = ''
max_occ = 0
for i in dic:
    if dic[i] > max_occ:
        max_occ = dic[i]
        max_key = i
        
print(max_key, max_occ)