a,b,c,d,u = map(int,input().split())
ans = max(0,(a<=u)+(u-a)//b)
while c<=u:
    if c < a or (c-a)%b:
        ans += 1
    c *= d
    if d == 1:
        break
print(ans)