n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.sort()
b.sort()
r = (n+1)//2
a = a[:r]
b = b[-r:]

print("NYOE S"[all(i<j for i,j in zip(a,b))::2])
    