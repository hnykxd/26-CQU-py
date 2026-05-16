m = list(map(float, input().split(' ')))
result = []
def no_rep(n):
    if len(str(n)) != 3:
        return False
    else:
        if str(n)[0]!= str(n)[1] and str(n)[1] != str(n)[2] and str(n)[0] != str(n)[2]:
            if m[0]<=n//100 < m[1] and m[0]<=(n//10)%10 < m[1] and m[0]<= n%10 < m[1]:
                
                return True
            else:
                return False
        else:
            return False
        
    
        
    
    
if m[0].is_integer() and m[1].is_integer() and m[0]<m[1]:
    for i in range (int(m[0])*100,int(m[1])*100):
        if no_rep(i):
            result.append(i)
            
    if len(result) == 0:
        print('illegal input')
    else:
        print(' '.join(str(x) for x in result))
else:
    print('illegal input')

# 优化版本
data = input().split()
if len(data) != 2:
    print('illegal input'); raise SystemExit

try:
    a_f, b_f = map(float, data)
except ValueError:
    print('illegal input'); raise SystemExit

if not (a_f.is_integer() and b_f.is_integer()):
    print('illegal input'); raise SystemExit

a, b = int(a_f), int(b_f)
if not (0 <= a < b <= 10):
    print('illegal input'); raise SystemExit

allowed = set(range(a, b))
start = max(100, a * 100)
end = min(1000, b * 100)  # range end is exclusive

result = []
for n in range(start, end):
    d1 = n // 100
    d2 = (n // 10) % 10
    d3 = n % 10
    if len({d1, d2, d3}) == 3 and d1 in allowed and d2 in allowed and d3 in allowed:
        result.append(n)

if result:
    print(' '.join(map(str, result)))
else:
    print('illegal input')