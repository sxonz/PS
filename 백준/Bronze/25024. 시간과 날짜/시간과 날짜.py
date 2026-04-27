m = [0,31,29,31,30,31,30,31,31,30,31,30,31]
for t in range(int(input())):
    x,y = map(int,input().split())
    if 0<=x<24 and 0<=y<60:
        print("Yes",end=' ')
    else:
        print("No",end=' ')
    if 1<=x<13 and 1<=y<=m[x]:
        print("Yes")
    else:
        print("No")