n = int(input())
d = list(map(int,input().split()))
d.sort()
print(sum(d)/2+d[-1]/2)