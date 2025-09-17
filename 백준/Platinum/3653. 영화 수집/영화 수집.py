import sys
input = sys.stdin.readline

testcase = int(input())
for test in range(testcase):
    n,m = map(int,input().split())
    query = list(map(int,input().split()))
    idx = {i:n-i+1 for i in range(1,n+1)}
    
    size = n+m+1
    cur = n+1
    bstree = [0]*size
    
    def build():
        for i in range(1,n+1):
            while i<size:
                bstree[i] += 1
                i += i&-i
                
    def search(num):
        x = idx[num]
        res = n
        while x:
            res -= bstree[x]
            x -= x&-x
        return res
    
    def update(pos):
        while pos < size:
            bstree[pos] += 1
            pos += pos&-pos
    
    def remove(num):
        x = idx[num]
        while x < size:
            bstree[x] -= 1
            x += x&-x
    
    ans = []
    build()
    for q in query:
        ans.append(search(q))
        remove(q)
        update(cur)
        idx[q] = cur
        cur += 1
    print(*ans)