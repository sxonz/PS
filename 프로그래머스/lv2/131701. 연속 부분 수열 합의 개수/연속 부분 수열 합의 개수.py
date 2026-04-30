from collections import deque
def solution(elements):
    answer = set()
    elements = deque(elements)
    def dfs(arr):
        temp = 0
        for i in arr:
            temp += i
            answer.add(temp)
    for i in range(len(elements)):
        elements.rotate(1)
        dfs(elements)
    return len(answer)