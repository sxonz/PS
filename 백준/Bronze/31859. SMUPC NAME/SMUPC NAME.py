n,name = input().split()
n = int(n)
c = 0
d  = set()
realname = ''
for i in range(len(name)):
    if name[i] in d:
        c +=1
    else:
        realname += name[i]
        d.add(name[i])
realname += str(c+4)
realname = str(n+1906) + realname
realname = ''.join([i for i in reversed(list(realname))])
print('smupc_'+realname)
