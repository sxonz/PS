import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    while True:
        if len(scoville) == 1:
            return cnt if scoville[0] >= K else -1
        f = heapq.heappop(scoville)
        if f >= K:
            break
        heapq.heappush(scoville, f + heapq.heappop(scoville)*2)
        cnt += 1
    return cnt
        
        
        
        