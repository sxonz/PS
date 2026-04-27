import sys
input = sys.stdin.readline
for t in range(int(input())):
    a,b,n = map(int,input().split())
    w = (n//2)*(a+b)+(n%2)*a
    h = (n//2)*(a+b)+(n%2)*b
    print(w*h)