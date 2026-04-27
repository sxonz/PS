d,flag=[],True
while True:
    l=list(map(int,input().split()))
    if flag:
        n=l.pop(0)
        flag = False
    for i in l:
        d.append(int(str(i)[::-1]))
    if not flag:
        if len(d) == n:
            break
print(*sorted(d),sep='\n')
