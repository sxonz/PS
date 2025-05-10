import sys
I,R=sys.stdin.readline,range
L,M=19,-1
P,D,m,last=[[0]*L],[[int(2e22)]*L],1,0
def adhoc(k,l):
    global m;x,y=[(k+last)%m],[l]
    for r in R(L-1):x+=[P[t:=x[M]][r]];y+=[y[M] + D[t][r]]
    P.append(x);D.append(y);m+=1
def query(x,l):
    global last
    for k in R(L-1,M,M):
        if l>=(d:=D[x][k]):l-=d;x=P[x][k]
    print(last:=x)
for q in R(int(I())):
    s,a,b = I().split();a,b=int(a),int(b)
    if"q"==s[0]:query(a,b)
    else:adhoc(a,b)