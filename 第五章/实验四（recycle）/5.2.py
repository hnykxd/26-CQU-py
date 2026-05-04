s1 = set(map(int, input().split(' ')))
s2 = set(map(int, input().split(' ')))

result1 = s1 ^ s2
result2 = s1 & s2
print(' '.join(str(x) for x in sorted(result1, reverse=True)))
print(' '.join(str(x) for x in sorted(result2, reverse=True)))