h,m,s = map(int,input().split(':'))
h2,m2,s2 = map(int,input().split(':'))
h3,m3,s3 = 0,0,0
for i in range(86401):
    s += 1
    s3 += 1
    if s3 == 60:
        s3 = 0
        m3 += 1
        if m3 == 60:
            m3 = 0
            h3 += 1
    if s == 60:
        s = 0
        m += 1
        if m == 60:
            m = 0
            h += 1
            if h == 24:
                h = 0
                
    if [s,m,h] == [s2,m2,h2]:
        break
h3 = '0'*(2-len(str(h3)))+str(h3)
m3 = '0'*(2-len(str(m3)))+str(m3)
s3 = '0'*(2-len(str(s3)))+str(s3)


print('{0}:{1}:{2}'.format(h3,m3,s3))