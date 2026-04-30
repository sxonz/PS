def r_change(n,radix):
    r = []
    while n > 0:
        n,mod = divmod(n,radix)
        r.append(str(mod))
    return ''.join(reversed(r))
    return ''.join(reversed(r))
def check(n):
    if n in [0,1]:
        return False
    if n in [2,3]:
        return True
    for i in range(2,int(n**0.5)+2):
        if n % i == 0:
            return False
    return True
def solution(n, k):
    rcnum = r_change(n,k)
    nums = rcnum.split('0')
    cnt = 0
    for i in nums:
        if i == '':continue
        if check(int(i)):
            cnt += 1
    return cnt
            