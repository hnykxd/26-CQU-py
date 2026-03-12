
data = list(map(float, input().split()))

# 变量解构
mid_score = data[0]      # 中期测试
lab_score = data[1]      # 综合实验
reg_score = data[2]      # 平时成绩
final_exam_score = data[3] # 期末成绩

total = mid_score * 0.1 + lab_score  + reg_score  + final_exam_score * 0.7

current_score = mid_score * 0.1 + lab_score  + reg_score

finalleast = (60 - current_score) / 0.7
print(f"{total:.1f}")
print(f"{finalleast:.1f}")

