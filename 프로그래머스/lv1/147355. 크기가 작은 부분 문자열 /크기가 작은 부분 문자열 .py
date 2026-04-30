def solution(t, p):
    n = []
    l = len(p)
    for i in range(len(t)-(len(p)-1)):
        n.append(t[i:i+l])
    n = list(map(int,n))
    return len([i for i in n if i <= int(p)])