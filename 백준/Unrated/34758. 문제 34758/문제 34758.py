x,y = map(int,input().split())
n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    print((a==x or b==y)^1)