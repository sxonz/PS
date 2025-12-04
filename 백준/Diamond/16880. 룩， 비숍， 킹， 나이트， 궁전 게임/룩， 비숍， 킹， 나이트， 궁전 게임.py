import sys
input = sys.stdin.readline

rooksize = 1073741824
palacesize = 1610612736

def rook(size,x,y,snum):
    if size == 1:
        return snum
    if (x<size//2) ^ (y<size//2):
        return rook(size//2,x%(size//2),y%(size//2),snum+size//2)
    return rook(size//2,x%(size//2),y%(size//2),snum)
def bishop(x,y):
    return min(x,y)
def king(x,y):
    return min(x,y)%2*2+(x+y)%2
def knight(x,y):
    if x == y:
        return max(x%3-1,0)
    if min(x,y)%3 == 2 and abs(x-y) == 1:
        return 1
    return min(x,y)%3
p = [[0,1,2],[1,2,0],[2,0,1]]
def palace(size,x,y,snum):
    if size == 3:
        return snum + p[x][y]
    elif (x<size//2) ^ (y<size//2):
        return palace(size//2,x%(size//2),y%(size//2),snum + size//2)
    else:
        return palace(size//2,x%(size//2),y%(size//2),snum)

# tlqkftlqkftlqkftlqkftlqkftlqkftlqkftlqkftlqkftlqkf
# x = [[[0,0,1,1],
#       [0,0,2,1],
#       [1,2,2,2],
#       [1,1,2,1]],
      
#       [[0,0,1,1],
#        [0,0,1,1],
#        [3,2,2,2],
#        [4,3,2,3]],
       
#        [[0,0,1,1],
#         [0,0,1,1],
#         [3,2,2,2],
#         [3,3,2,3]]]
# y = [[[0,0,1,1],
#       [0,0,2,1],
#       [1,2,2,2],
#       [1,1,2,1]],
      
#        [[0,0,3,4],
#         [0,0,2,3],
#         [1,1,2,2],
#         [1,1,2,3]],
        
#         [[0,0,3,3],
#        [0,0,2,3],
#        [1,1,2,2],
#        [1,1,2,3]],]
# def knight(x,y):
#     if x//4 == y//4:
#         return x[x%4][y%4]
# x0 x2 x1 x1 x1 x1 x1 x1
# y2 x0 x2 x1 x1 x1 x1 x1
# y1 y2 x0 x2 x1 x1 x1 x1
# y1 y1 y2 x0 x2 x1 x1 x1
# y1 y1 y1 y2 x0 x2 x1 x1
# y1 y1 y1 y1 y2 x0 x2 x1
# y1 y1 y1 y1 y1 y2 x0 x2
# y1 y1 y1 y1 y1 y1 y2 x0

n = int(input())
res = 0
for i in range(n):
    x,y,r = input().split()
    x,y = int(x),int(y)
    if r == "R":
        res ^= rook(rooksize,x,y,0)
    elif r == "B":
        res ^= bishop(x,y)
    elif r == "K":
        res ^= king(x,y)
    elif r == "N":
        res ^= knight(x,y)
    else:
        res ^= palace(palacesize,x,y,0)
if res:
    print("koosaga")
else:
    print("cubelover")