n,m = map(int,input().split())
if m:
    d = list(map(int,input().split()))
else:
    d = []

cur = []
def back(c):
    if c == n:
        for i in d:
            if i not in cur:
                return 0
        return 1
    tmp = 0
    for i in range(10):
        cur.append(i)
        tmp += back(c+1)
        cur.pop()
    return tmp
print(back(0))
    