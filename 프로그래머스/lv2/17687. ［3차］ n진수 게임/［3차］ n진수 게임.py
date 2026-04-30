def solution(n, t, m, p):
    result,p,t = "0",p-1,t*m
    for i in range(1,t):
        result += radix_change(i,n)
    result = [result[i] for i in range(p,t,m)]
    return "".join(result)
def radix_change(num,n):
    changed = ""
    temp = [10,11,12,13,14,15,16]
    while num != 0:
        num, mod = divmod(num, n)
        if n in temp[1:] and mod in temp[:-1]:
            changed += "ABCDEF"[mod % 10]
        else:
            changed += str(mod)
    return changed[::-1]