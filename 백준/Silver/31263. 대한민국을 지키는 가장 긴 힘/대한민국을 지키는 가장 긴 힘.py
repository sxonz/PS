n = int(input())
s = input()
MAXDAY = 641
INF = int(1e9)
cache = [INF]*(n+1)
cache[0] = 0
for i in range(1, n+1):
    for length in range(1, 4):
        if i - length < 0:
            continue
        segment = s[i-length:i]
        if segment[0] == '0':
            continue
        if int(segment) > MAXDAY:
            continue
        cache[i] = min(cache[i], cache[i-length] + 1)

print(-1 if cache[n] == INF else cache[n])
