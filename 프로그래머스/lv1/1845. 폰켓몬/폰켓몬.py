def solution(nums):
    lnums = list(set(nums))
    sum = int(len(nums) / 2)
    return min(sum,len(lnums))