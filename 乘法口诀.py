def dajiujiu(n):
    nums = [[f"{x}×{y}={x*y}" for x in range(1, n+1)] for y in range(1, n+1)]
    for num in nums:
        print(num)
        
n = int(input())
dajiujiu(n)