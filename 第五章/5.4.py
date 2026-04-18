s =eval(input())
j = 0
for i in range(len(s)):
    if s[i] != 0 :
        s[i],s[j] = s[j], s[i]
        j += 1
print(s)