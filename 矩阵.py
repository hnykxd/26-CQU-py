def multiply(a,b,p,q,r):
    result = [[0 for _ in range(r)] for _ in range(p)]
    for k in range(q):
        for i in range(p):
            for j in range(r):
                result[i][j] += a[i][k]*b[k][j]

    return result

p = int(input())
q = int(input())
r = int(input())

a = [[x for x in range(q)] for y in range(p)]
b = [[x*y for x in range(r)] for y in range(q)]
c = multiply(a,b,p,q,r)  

for x in c:
    print(x)