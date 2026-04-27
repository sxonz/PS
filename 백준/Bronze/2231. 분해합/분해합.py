n = int(input())
S = lambda x:x + sum([int(i) for i in str(x)])
for i in range(n):
    if S(i) == n:
        print(i)
        break
else:
    print(0)
