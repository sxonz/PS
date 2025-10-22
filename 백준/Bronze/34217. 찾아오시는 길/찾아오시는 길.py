a,b = map(int,input().split())
c,d = map(int,input().split())
e = a+c
f = b+d
print("Hanyang Univ."*(e<f)+"Either"*(e==f)+"Yongdap"*(e>f))