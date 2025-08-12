import sys
input = sys.stdin.readline
def T(s):
    return int(s[:2])*60 + int(s[3:])
S,E,Q = input().split()
S,E,Q = T(S), T(E), T(Q)

res = set()
ans = 0
while True:
    try:
        time, name = input().split()
        time = T(time)

        if time <= S:
            res.add(name)
        elif name in res and (E<=time<=Q):
            res.remove(name)
            ans += 1
    except:
        print(ans)
        break