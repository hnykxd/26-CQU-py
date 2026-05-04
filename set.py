def missNumber(nums):
    n = set(x for x in range(len(nums)+1))
    for x in nums:
        n.discard(x)
    return n.pop()