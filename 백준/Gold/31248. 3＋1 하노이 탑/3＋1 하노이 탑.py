D = 'D'
move = []
def dfs(s,e,m,depth):
    if depth == 0:
        return
    if depth == 1:
        move.append((s,e))
        return
    dfs(s,m,e,depth-1)
    move.append((s,e))
    dfs(m,e,s,depth-1)


def d(s,e,m,depth):
    if depth == 0:
        return
    if depth == 1:
        move.append((s,D))
        return
    dfs(s,e,m,depth-2)
    move.append((s,m))
    move.append((s,D))
    move.append((m,D))
    d(e,m,s,depth-2)


n = int(input())
d('A','C','B',n)
print(len(move))
for i in move:
    print(' '.join(i))