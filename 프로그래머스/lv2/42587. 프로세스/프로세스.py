from collections import deque

def solution(priorities, location):
    queue = deque(enumerate(priorities))
    answer = 0
    
    while True:
        idx, priority = queue.popleft()
        if any(priority < p for _, p in queue):
            queue.append((idx, priority))
        else:
            answer += 1
            if idx == location:
                return answer