def solution(lines):
    d = []
    for i in lines:
        d.append((i[0]+100,i[1]+100))
    l = [0]*201
    for a,b in d:
        print(a,b)
        for i in range(a,b):
            l[i] += 1
    return sum(max(min(1,i-1),0) for i in l)