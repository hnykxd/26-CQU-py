s = eval(input())
a = max(s)
b = min(s)
s1 = [ch for ch in s if ch != a and ch !=b]
print(s1)