m = int(input())
n = int(input())
B = (6*n-8*m)/(n-m)
A = 8*m - m*B
C = A/(10 - B)
print(f"原有排队游客份数:{A:.1F}, 每分钟新到游客份数:{B:.1F}, 10口同开需{C:.1F}分钟清零待检票游客.")

