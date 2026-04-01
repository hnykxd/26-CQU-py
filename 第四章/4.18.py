credit_all = 0
gpasum = 0
for i in range(5):
    s = input().split()
    lst = list(s)
    score = float(lst[1])
    credit = float(lst[2])
    gpa = 4.0*(90 if score > 90 else score)/90
    credit_all += credit
    sum = gpa*credit
    gpasum += sum

GPA = gpasum/credit_all

print(f"GPA:{GPA:.2f}")
