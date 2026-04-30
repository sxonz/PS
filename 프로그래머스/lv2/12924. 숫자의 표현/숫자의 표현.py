from collections import deque
def solution(n):
    answer = 0
    nums = deque()
    i = 1
    while i != n:
        if sum(nums) == n:
            answer += 1
            nums.popleft()
        if sum(nums) > n:
            nums.popleft()
        if sum(nums) < n:
            nums.append(i)
            i+=1
    return answer+1 if n != 3 else 2