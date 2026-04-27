n,m = map(int,input().split())
songs = dict()
for _ in range(n):
    l,song,a,b,c,d,e,f,g = input().split()
    temp = a+b+c
    if temp in songs:
        songs[temp].append(song)
    else:
        songs[temp] = [song]
for _ in range(m):
    quiz = input().replace(' ','')
    if not(quiz in songs):
        print('!')
    else:
        if len(songs[quiz]) >= 2:
            print('?')
        else:
            print(''.join(songs[quiz]))