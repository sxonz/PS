from collections import deque

def change(x):
    if x not in range(0,100):
        return ord(x)-65 if x != '.' else -1
    else:
        return chr(x+65)



def s1(x):
    d1.append(x)
    if graph[x][0] != -1:
        s1(graph[x][0])
    if graph[x][1] != -1:
        s1(graph[x][1])


def s2(x):
    if graph[x][0] != -1:
        s2(graph[x][0])
    d2.append(x)
    if graph[x][1] != -1:
        s2(graph[x][1])


def s3(x):
    if graph[x][0] != -1:
        s3(graph[x][0])
    if graph[x][1] != -1:
        s3(graph[x][1])
    d3.append(x)

n = int(input())
#65~90
graph = [[] for _ in range(n)]
for i in range(n):
    p,l,r = map(change,input().split())
    graph[p].append(l)
    graph[p].append(r)

d1,d2,d3 = [],[],[]

s1(0);s2(0);s3(0)
print(''.join(list(map(change,d1))))
print(''.join(list(map(change,d2))))
print(''.join(list(map(change,d3))))