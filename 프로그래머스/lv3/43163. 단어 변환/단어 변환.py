from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0
    answer = 0
    queue = deque([[begin,0,[]]])
    
    while queue:
        current,count,visit = queue.popleft()
        print(current,count,visit)
        if current == target:
            return count
        for i in words:
            if i not in visit and sum([1 for j,k in zip(i,current) if j != k]) == 1:
                visit.append(i)
                queue.append([i,count + 1,visit])
        
    