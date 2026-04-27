import sys
input = sys.stdin.readline
v = dict()
for i in range(26):
    v[chr(i+97)] = i
s = input().strip()
n = len(s)
m = int(input())
prefix_sum = [[0]*26 for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(26):
        prefix_sum[i][j] = prefix_sum[i-1][j]
    prefix_sum[i][v[s[i-1]]]+=1
for i in range(m):
    c,a,b = input().split()
    a,b = int(a),int(b)
    print(prefix_sum[b+1][v[c]]-prefix_sum[a][v[c]])