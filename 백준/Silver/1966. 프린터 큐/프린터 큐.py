from collections import deque
for t in range(int(input())):
    n,q = map(int,input().split())
    d = deque(map(int,input().split()))
    cnt = 0
    while True:
        r = d.popleft()
        if not d or r >= max(d):
            cnt += 1
            if q == 0:
                print(cnt)
                break
            q -= 1
            continue
        d.append(r)
        if q == 0:
            q = len(d)
        q -= 1
