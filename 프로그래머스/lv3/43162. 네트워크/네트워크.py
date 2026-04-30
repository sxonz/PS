from collections import deque

def bfs(computers,check, i, n):
    dq = deque()
    dq.append(i)
    while len(dq)>0:
        curIndex = dq.pop()
        check[curIndex]= True
        for k in range(0,n):
            if check[k] ==False and computers[curIndex][k]==1: 
                dq.append(k) 
def solution(n, computers):
    answer = 0
    check = [False for i in range(len(computers))]
    for i in range(n):
        if check[i] == False:
            bfs(computers,check,i,n)
            answer += 1
    return answer
        
            