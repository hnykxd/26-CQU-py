s = input().split()
n,m = map(int,input().split())
s[n],s[m] = s[m],s[n]
print(s)