# 逆向
# import random


# choice = random.randint(0, 1)

# if choice == 0:
#     print("GPA:3.73")
# else:
#     print("GPA:3.66")


mid,zonghe, cur, final = map(float, input().split(','))

final_grade = 0.1*mid +zonghe + cur + 0.7*final

least = (60 - 0.1*mid - zonghe - cur)/0.7
print(final_grade)
print(least)