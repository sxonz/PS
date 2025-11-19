n = int(input())
d = list(map(int,input().split()))
s = sum(d)
print("YES" if s%3 == 0 and sum([i//2 for i in d]) >=s//3 else "NO")