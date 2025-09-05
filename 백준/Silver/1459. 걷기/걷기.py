x,y,w,s = map(int,input().split())
print(min(x,y)*min(s,2*w)+abs(x-y)//2*min(w,s)*2+abs(x-y)%2*w)