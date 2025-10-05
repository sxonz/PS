tr = [[" "," ","*"," "," "],[" ","*"," ","*"," "],["*","*","*","*","*"]]

n = int(input())
d = [[' ']*(n*2) for i in range(n)]
def divide(x,y,size):
    if size == 3:
        for i in range(3):
            for j in range(5):
                d[x+i][y+j] = tr[i][j]
        return
    divide(x,y+size//2,size//2)
    divide(x+size//2,y,size//2)
    divide(x+size//2,y+size,size//2)
divide(0,0,n)
for i in d:
    print(*i,sep='')