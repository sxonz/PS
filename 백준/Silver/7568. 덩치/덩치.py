n = int(input())
d = [tuple(map(int,input().split())) for i in range(n)]
print(*[1+sum([j[0] > i[0] and j[1] > i[1] for j in d]) for i in d])