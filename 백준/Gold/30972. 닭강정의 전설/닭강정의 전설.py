import sys
input = sys.stdin.readline

n = int(input())
psum = [[0]*(n+1)] + [[0]+list(map(int,input().split())) for i in range(n)]

for i in range(n):
    for j in range(n):
        psum[i+1][j+1] += psum[i][j+1] + psum[i+1][j] - psum[i][j]

for q in range(int(input())):
    a,b,c,d = map(int,input().split())
    print(-psum[c][d] + psum[a-1][d] + psum[c][b-1] - psum[a-1][b-1] + 2*(psum[c-1][d-1] - psum[a][d-1] - psum[c-1][b] + psum[a][b]))