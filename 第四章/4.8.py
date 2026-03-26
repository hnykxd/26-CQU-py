s1 = input()
s2 = input()
lst1 = list(s1)
lst2 = list(s2)
lst1.sort()
lst2.sort()
if lst1 == lst2:
    print("True")
else:
    print("False")