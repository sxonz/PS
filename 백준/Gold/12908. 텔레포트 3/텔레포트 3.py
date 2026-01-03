from itertools import permutations
def S(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)
sx,sy = map(int,input().split())
ex,ey = map(int,input().split())
tel = [0]+[list(map(int,input().split())) for i in range(3)]
for i in tel[1:]:
    tel.append([i[2],i[3],i[0],i[1]])
ans = S(sx,sy,ex,ey)
for i in 1,4,2,5,3,6:
    ans = min(ans,S(sx,sy,tel[i][0],tel[i][1])+S(tel[i][2],tel[i][3],ex,ey)+10)

for i in permutations(range(1,7),2):
    if (1 in i and 4 in i) or (2 in i and 5 in i) or (3 in i and 6 in i):
        continue
    ans = min(ans,S(sx,sy,tel[i[0]][0],tel[i[0]][1])+S(tel[i[0]][2],tel[i[0]][3],tel[i[1]][0],tel[i[1]][1])+S(tel[i[1]][2],tel[i[1]][3],ex,ey)+20)
for i in permutations(range(1,7),3):
    if (1 in i and 4 in i) or (2 in i and 5 in i) or (3 in i and 6 in i):
        continue
    ans = min(ans,S(sx,sy,tel[i[0]][0],tel[i[0]][1])+S(tel[i[0]][2],tel[i[0]][3],tel[i[1]][0],tel[i[1]][1])+S(tel[i[1]][2],tel[i[1]][3],tel[i[2]][0],tel[i[2]][1])+S(tel[i[2]][2],tel[i[2]][3],ex,ey)+30)
print(ans)