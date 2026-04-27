d = list(map(int,input().split()))
ans = 0
for d1 in range(16):
    for d2 in range(8):
        for d3 in range(6):
            for d4 in range(4):
                for d5 in range(4):
                    if d1+d2+d3+d4+d5 <= 3:
                        if d1*1+d2*2+d3*3+d4*4+d5*5 > 10:
                            continue
                    else:
                        if d1*1+d2*2+d3*3+d4*4+d5*5 > 15:
                            continue
                    ans = max(ans,d1*d[0]+d2*d[1]+d3*d[2]+d4*d[3]+d5*d[4])
print(ans)
