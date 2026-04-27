n = int(input())
d = [input() for _ in range(n)]

def f(size,idx,first,last):
    x,y = idx
    temp = []

    if size == 1:
        return d[x][y]

    for i in range(2):
        for j in range(2):
            ns = size // 2
            nx = x + i*ns
            ny = y + j*ns
            t = f(ns,(nx,ny), i==0 and j==0, i==1 and j==1)

            temp.append(t)
    flag = True
    num = 2
    test = temp[0]
    if len(test) > 2:
        flag = False
    if flag:
        for i in temp:
            if i != test:break
        else:
            temp = t
    
    return temp

result = str(f(n,(0,0),True,False))
for b,a in zip(["'",'[',']',',',' '], ['','(',')','','']):
    result = result.replace(b,a)

print(result)