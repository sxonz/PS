from collections import deque
def solution(A, B):
    temp,temp2 = deque(A),deque(B)
    for i in range(len(A)):
        if str(temp) == str(temp2):
            return i
        temp.rotate(1)
    return -1