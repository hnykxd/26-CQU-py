dic = {}
lst = []
with open("data2.txt", "r") as f:
    for line in f:
        line = line.split()
        fruit, count = line[0],line[1]
        dic[fruit] = dic.get(fruit,0) + int(count)

for i in dic.keys():
    if dic[i] == max(dic.values()):
        lst.append(i)  
    
lst.sort
for i in lst:
    print(i)