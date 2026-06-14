dic = {}
with open("in.txt","r") as f:
    for line in f:
        line = line.split(" ")
        for i in line:
            dic[i] = dic.get(i,0) + 1
lst = []
paixu = sorted(dic.items(),key = lambda x :(-x[1],x[0]))
with open("out.txt","w") as f:
    for i in paixu:
        f.write(i[0] + " " + str(i[1]) + "\n")