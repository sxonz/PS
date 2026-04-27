dp = [[[0]*21 for i in range(21)] for j in range(21)]
def r(x,y,z):
    if x<=0 or y<=0 or z<=0:
        return 1
    if x>20 or y>20 or z>20:
        return r(20,20,20)
    if dp[x][y][z]:
        return dp[x][y][z]
    if x < y < z:
        dp[x][y][z] = r(x,y,z-1) + r(x,y-1,z-1) - r(x,y-1,z)
    else:
        dp[x][y][z] = r(x-1,y,z) + r(x-1,y-1,z) + r(x-1,y,z-1) - r(x-1,y-1,z-1)
    return dp[x][y][z]
while True:
    a,b,c = map(int,input().split())
    if [a,b,c] == [-1,-1,-1]:
        break
    print(f'w({a}, {b}, {c}) = {r(a,b,c)}')