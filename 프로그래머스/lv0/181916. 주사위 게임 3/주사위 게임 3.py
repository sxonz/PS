def check(nums):
    maxnum = 1
    for i in set(nums):
        if nums.count(i) > maxnum:
            maxnum = nums.count(i)
    return maxnum
def maxcheck(nums):
    maxnum = 1
    for i in set(nums):
        if nums.count(i) > maxnum:
            maxnum = i
    return maxnum
def onenum(nums):
    for i in nums:
        if nums.count(i) == 1:
            return i
def jcheck(nums):
    return len(set(nums))
def abstract(nums):
    return max(nums) - min(nums)
def onenums(nums):
    onenums = []
    for i in nums:
        if nums.count(i) == 1:
            onenums.append(i)
    return onenums
def solution(a, b, c, d):
    temp = [a,b,c,d]
    k = check(temp)
    if k == 4:
        return a * 1111
    elif k == 3:
        return (10 * maxcheck(temp) + onenum(temp)) ** 2
    elif k == 2 and jcheck(temp) == 2:
        return sum([i for i in set(temp)]) * abstract(set(temp))
    elif k == 2 and jcheck(temp) == 3:
        return onenums(temp)[0] * onenums(temp)[1]
    elif k == 1:
        return min(temp)
        