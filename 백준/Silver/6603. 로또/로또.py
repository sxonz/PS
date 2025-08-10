from itertools import combinations
while True:

    k, *d= list(map(int, input().split()))

    if not k:
        break

    for i in combinations(d, 6):
        print(*i)
    print()