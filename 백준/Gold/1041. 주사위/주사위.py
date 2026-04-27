n = int(input())
d = list(map(int,input().split()))
trio = [[0,1,2],[0,1,3],[0,2,4],[0,3,4],[1,2,5],[1,3,5],[2,4,5],[3,4,5]]
duo = [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,5],[2,4],[2,5],[3,4],[3,5],[4,5]]
mtrio = min([d[i]+d[j]+d[k] for i,j,k in trio])
mduo = min([d[i]+d[j] for i,j in duo])
mpenta = sum(d) - max(d)
res = mtrio*4 + mduo*(8*(n-2)+4) + min(d)*(n*n*5 - 12 - (16*(n-2)+8)) if n != 1 else mpenta
print(res)
