a1,a0 = map(int,input().split())
c = int(input())
n = int(input())
print(int(c >= a1 and a1*n+a0 <= c*n))