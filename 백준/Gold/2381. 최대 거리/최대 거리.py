n = int(input())
d = [tuple(map(int,input().split())) for _ in range(n)]
print(max(max([x+y for x,y in d])-min([x+y for x,y in d]),max([x-y for x,y in d])-min([x-y for x,y in d])))