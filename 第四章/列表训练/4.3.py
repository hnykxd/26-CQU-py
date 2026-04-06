s = eval(input())

result = [x for x in s if x != 0]
result.extend([0] * (len(s) - len(result)))

print(result)
        