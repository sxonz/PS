def s(x1, y1, r1, x2, y2, r2):
    if x1 == x2 and y1 == y2 and r1 == r2:
        return -1

    dist = (abs(x1-x2)**2 + abs(y1-y2)**2)**0.5

    if dist+r1 < r2 or dist+r2 < r1 or dist > r1+r2:
        return 0
    if dist+r1 == r2 or dist+r2 == r1 or dist == r1+r2:
        return 1
    return 2


n = int(input())

for i in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    print(s(x1, y1, r1, x2, y2, r2))