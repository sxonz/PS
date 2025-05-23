def p(x):
    div = []
    for i in range(1,min(int(x**0.5)+1,10000000)):
        if x%i == 0:
            div.append(i)
            if x//i <= 1e7 and i != 1:
                div.append(x//i)
    return max(div)
def solution(begin, end):
    r = []
    for i in range(begin,end+1):
        if i in [1,2]:
            r.append(i-1)
            continue
        r.append(p(i))
    return r