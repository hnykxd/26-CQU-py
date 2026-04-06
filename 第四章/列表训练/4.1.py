s = eval(input())
s.sort(reverse = True)
s = [str(x) for x in s]
maxs = ''.join(s)
maxsum = int(maxs)
print(maxsum)