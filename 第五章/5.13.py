s = [int(x) for x in input()]
result = []
for i in range(len(s)):
    result.append((s[i]+5)%10)
result.reverse()
print(''.join(map(str, result)))
