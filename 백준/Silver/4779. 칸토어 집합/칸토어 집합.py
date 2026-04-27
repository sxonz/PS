def solve(l,r,size):
    if size == 1:
        d[l] = "-"
        return
    solve(l,l+size//3-1,size//3)
    solve(r-size//3+1,r,size//3)
try:
    while True:
        n = 3**int(input())
        d = [' ']*n
        solve(0,n-1,n)
        print(''.join(d))
except:
    pass