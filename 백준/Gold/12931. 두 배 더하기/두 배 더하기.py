n = int(input())
d = list(map(int,input().split()))
cnt = 0
while sum(d):
    cnt += sum([i%2 for i in d])
    d = [i-i%2 for i in d]
    if not sum(d):
        break
    d = [i//2 for i in d]
    cnt += 1
print(cnt)