def solution(keyinput, board):
    col = board[0]
    row = board[1]
    answer = [0,0]
    for i in keyinput:
        if i == "up" and answer[1] + 1 <= (row // 2):
            answer[1] += 1
        elif i == "down" and answer[1] - 1 >= 0 - (row // 2):
            answer[1] -= 1
        elif i == "left" and answer[0] - 1 >= 0 - (col // 2):
            answer[0] -= 1
        elif i == "right" and answer[0] + 1 <= (col // 2):
            answer[0] += 1
    return answer