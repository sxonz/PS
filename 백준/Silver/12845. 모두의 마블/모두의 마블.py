n = int(input())
d = list(map(int,input().split()))
d.sort(reverse=True)
print((n-2)*d[0]+sum(d))