def check(a,b,size):
    cnt = 0
    for i in range(size):
        for j in range(i+1):
            cnt += int(a[i][j] != b[i][j])
    return cnt

def rotate(a,size):
    tmp = []
    for i in range(size):
        s = []
        for j in range(i+1):
            s.append(0)
        tmp.append(s)
    for i in range(size):
        for j in range(i+1):
            x = size-i-1+j
            y = size-i-1
            tmp[x][y] = a[i][j]
    return tmp
def rev(a):
    tmp = [0]*len(a)
    for i in range(len(a)):
        tmp[i] = list(reversed(a[i]))
    return tmp

n = int(input())


t1 = []
for i in range(n):
    t1.append(list(map(int,input().split())))

t2 = []
for i in range(n):
    t2.append(list(map(int,input().split())))

case = []
case.append(t1)
revt = rev(t1)
case.append(revt)
case.append(rotate(t1,n))
case.append(rotate(revt,n))
case.append(rotate(rotate(t1,n),n))
case.append(rotate(rotate(revt,n),n))

m = 3141592
for i in case:
    m = min(check(i,t2,n),m)
print(m)