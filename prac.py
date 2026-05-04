def find_nums(n):
    lst = []
    for i in range(1, n):
        if i % 3 == 0 or ('7' in str(i) or i % 7 == 0):
            lst.append(i)
    result = ' '.join(str(x) for x in lst)
    print(result)
    return 

n = int(input())
find_nums(n)