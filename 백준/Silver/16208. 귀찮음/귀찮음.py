n = int(input())
d = list(map(int,input().split()))
r = sum(d)
print(sum((r:=r-i)*i for i in sorted(d)))