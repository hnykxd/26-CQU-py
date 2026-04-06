s = eval(input())

seen = set()
result = []

for item in reversed(s):
    if item not in seen:
        result.append(item)
        seen.add(item)
    

result.reverse()
    
print(result)