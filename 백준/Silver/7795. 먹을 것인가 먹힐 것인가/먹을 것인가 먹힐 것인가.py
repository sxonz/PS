import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    cnt = 0
    for i in a:
        s, e = 0, m-1
        while s <= e:
            mid = (s + e) // 2
            if b[mid] < i:
                s = mid + 1
            else:
                e = mid - 1
        cnt += s
    print(cnt)