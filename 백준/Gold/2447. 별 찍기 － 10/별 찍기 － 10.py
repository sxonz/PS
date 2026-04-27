n = int(input())

def star(size,idx,ismiddle):
    temp = [[' ']*size for _ in range(size) ]
    if ismiddle:
        return temp
    if size == 1:
        return ['*']
    x,y = idx
    for i in range(3):
        for j in range(3):
            ns = size // 3
            nx = x + ns*i
            ny = y + ns*j
            t = star(ns,(nx,ny),i == 1 & j == 1)
            for k in range(len(t)):
                for l in range(len(t)):
                    temp[(nx+k) % size][(ny+l) % size] = t[k][l]

    return temp

d = star(n,(0,0),False)

for i in d:
    print(''.join(i))