s = []
with open("score.txt","r") as f:
    for line in f:
        info = line.split(",")
        name = info[0]
        sid = info[1]
        grade1 = int(info[2])
        grade2 = int(info[3])
        grade3 = int(info[4])
        total = grade1+grade2+grade3
        s.append([sid,name,grade1,grade2,grade3,total])
        
s.sort(key = lambda x :x[5],reverse = True)

with open("sorted.txt","w") as f:
    for i in s:
        f.write(i[0] + ',' + i[1] + ',' + str(i[2]) + ',' + str(i[3]) + ',' + str(i[4]) + "\n")

