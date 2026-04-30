def quad(size,d):
    if size == 1:
        return [d[0][0]]
    dx = ((0,size//2),(size//2,size),(0,size//2),(size//2,size))
    dy = ((0,size//2),(0,size//2),(size//2,size),(size//2,size))
    bn = []
    for k in range(4):
        nd = []
        for i in range(dx[k][0],dx[k][1]):
            tmp = []
            for j in range(dy[k][0],dy[k][1]):
                tmp.append(d[i][j])
            nd.append(tmp)
        s = quad(size//2,nd)
        if len(set(s)) == 1:
            bn += [s[0]]
        else:
            bn += s
    return bn
def solution(arr):
    r = len(arr)
    res = quad(r,arr)
    res = [res.count(0),res.count(1)]
    if res == [4,0]:
        res = [1,0]
    if res == [0,4]:
        res = [0,1]
    return res