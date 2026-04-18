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

    