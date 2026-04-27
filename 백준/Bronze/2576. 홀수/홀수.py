d = [int(input()) for _ in range(7)]
d = [i for i in d if i % 2 != 0]
if d:
    print(sum(d))
    print(min(d))
else:
    print(-1)