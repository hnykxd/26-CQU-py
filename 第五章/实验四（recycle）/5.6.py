n = int(input())
goodgoodstudydaydayup = 1
sleeeeeeeeeeeeeeeeeep = 1
for _ in range(n):
    goodgoodstudydaydayup += goodgoodstudydaydayup*0.005
    sleeeeeeeeeeeeeeeeeep -= sleeeeeeeeeeeeeeeeeep*0.001
    
print(f"{goodgoodstudydaydayup:.2f} - {sleeeeeeeeeeeeeeeeeep:.2f} = {goodgoodstudydaydayup - sleeeeeeeeeeeeeeeeeep:.2f}")