from itertools import permutations
def check(n):
    if n == 1:
        return False
    if n in [2,3]:
        return True
    for i in range(2,int(n**0.5)+2):
        if n % i == 0:
            return False
    return True
def solution(numbers):
    cnt = 0
    nums = set()
    for i in range(len(numbers)):
        for j in permutations(list(numbers),i+1):
            nums.add(''.join(j).lstrip('0'))
    for i in nums:
        if i == '':
            continue
        if check(int(i)):
            cnt += 1
    return cnt
        